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

    class Meta:
        model = Product
        fields = ['name', 'description', 'sku', 'stock', 'image']
        
        image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        