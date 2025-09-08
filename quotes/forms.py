from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'source', 'weight']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }