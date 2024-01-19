from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']
        widgets = {
            'product': forms.Select(),
            'rating': forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}),
            'comment': forms.Textarea(),
        }