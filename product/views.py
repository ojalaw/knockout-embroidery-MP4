from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm, ProductForm
from django.http import HttpResponseForbidden


def reviews(request):
    """ reviews view """
    all_reviews = Review.objects.all().order_by('-date_posted')
    context = {
        'reviews': all_reviews,
    }
    return render(request, 'product/reviews.html', context)


@login_required
def add_review(request):
    """ A view that allows users to add reviews """
    request.session['show_basket_in_toast'] = False
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('reviews')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
    else:
        form = ReviewForm()

    return render(request, 'product/add_reviews.html', {'form': form})


@login_required
def update_review(request, review_id):
    """ A view that handles updating user reviews """
    review = get_object_or_404(Review, pk=review_id)

    if request.user != review.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
            return redirect('reviews')
        else:
            messages.error(request, 'Error updating your review.')

    else:
        form = ReviewForm(instance=review)

    return render(request, 'product/reviews.html', {'form': form,
                                                        'review': review})


@login_required
def delete_review(request, review_id):
    """ A view that allows users to delete reviews """
    review = get_object_or_404(Review, pk=review_id)

    if request.user == review.user or request.user.is_superuser:
        review.delete()
        messages.success(request, "Your review has been deleted.")
    else:
        messages.error(request, "You do not have permission to delete this.")

    return redirect('reviews')


def products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'product/product.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)


def product_reviews(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'product/reviews.html', {'reviews': reviews,
                                                    'product': product})


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the'
                           'form is valid.')
    else:
        form = ProductForm()

    template = 'product/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.'
                                    'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'product/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
