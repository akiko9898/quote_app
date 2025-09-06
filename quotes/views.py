from django.shortcuts import render
from .models import Quote
import random

def random_quote(request):
    quotes = Quote.objects.all()
    if quotes.exists():
        quote = random.choice(quotes)
    else:
        quote = None
    return render(request, 'quotes/random_quote.html', {'quote': quote})