from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Quote

class QuoteModelTest(TestCase):
    def test_save_with_duplicate_text(self):
        Quote.objects.create(text="Test text", author="Test author", source="Test source", weight=1)
        quote = Quote(text="Test text", author="Test author", source="Test source", weight=1)
        with self.assertRaises(ValidationError):
            quote.clean()