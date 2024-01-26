from django import forms
from .models import Review, Product
from .widgets import CustomClearableFileInput

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Review Title'})
        self.fields['comment'].widget.attrs.update({'placeholder': 'Enter your review here'})


class ProductForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    embroidery_text = forms.CharField(max_length=120, required=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'sku', 'stock', 'image', 'embroidery_location', 'embroidery_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['embroidery_text'].widget.attrs.update({'maxlength': '147'})
