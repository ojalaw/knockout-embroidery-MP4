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
        

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        
        image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        