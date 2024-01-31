from django import forms
from django.core.exceptions import ValidationError
from .models import Review, Product
from .widgets import CustomClearableFileInput


class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=80, required=True, widget=forms.
                            TextInput(attrs={'placeholder': 'Review Title'}))
    comment = forms.CharField(max_length=255, required=True, widget=forms.
                          Textarea(attrs={'placeholder': 'Enter your review'
                                          'here', 'rows': 4}, ))
    rating = forms.IntegerField(required=True) 

    class Meta:
        model = Review
        fields = ['title', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(),
        }

        def clean_comment(self):
            comment = self.cleaned_data.get('comment')
            if len(comment) > 255:
                raise ValidationError("Comment cannot exceed 255 characters.")
            return comment

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Review Title',
            'aria-label': 'Review Title'
        })
        self.fields['comment'].widget.attrs.update({
            'placeholder': 'Enter your review here',
            'aria-label': 'Review Comment'
        })


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock', 'sku',  'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
