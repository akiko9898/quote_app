from django import forms
from .models import Source, Quote

class QuoteForm(forms.ModelForm):
    source_name = forms.CharField(max_length=200, label="Название источника")
    source_type = forms.ChoiceField(choices=[('movie', 'Фильм'), ('book', 'Книга')], label="Тип источника")

    class Meta:
        model = Quote
        fields = ['text', 'weight']
        labels = {'text': 'Текст цитаты', 'weight': 'Вес цитаты'}

    def clean(self):
        cleaned_data = super().clean()
        source_name = cleaned_data.get('source_name')
        source_type = cleaned_data.get('source_type')
        text = cleaned_data.get('text')

        # Проверка или создание источника
        source, created = Source.objects.get_or_create(name=source_name, type=source_type)
        if source.quote_count() >= 3:
            raise forms.ValidationError(f"У источника '{source_name}' уже есть 3 цитаты.")
        if Quote.objects.filter(text=text).exists():
            raise forms.ValidationError("Эта цитата уже существует.")
        cleaned_data['source'] = source
        return cleaned_data