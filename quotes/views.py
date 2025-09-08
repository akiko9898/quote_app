from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Quote
from .forms import QuoteForm
import random

def random_quote(request):
    if request.method == 'POST':
        quote_id = request.POST.get('quote_id')
        action = request.POST.get('action')
        quote = Quote.objects.get(id=quote_id)
        if action == 'like':
            quote.likes += 1
        elif action == 'dislike':
            quote.dislikes += 1
        quote.save()
        return redirect('random_quote')

    quotes = Quote.objects.all()
    if quotes:
        quote = random.choices(quotes, weights=[q.weight for q in quotes])[0]
        quote.views += 1
        quote.save()
    else:
        quote = None
    return render(request, 'quotes/random_quote.html', {'quote': quote})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            try:
                form.instance.clean()
                form.save()
                return redirect('random_quote')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def top_quotes(request):
    source_filter = request.GET.get('source', '')
    sort_by = request.GET.get('sort_by', '-likes')
    quotes = Quote.objects.all()
    if source_filter:
        quotes = quotes.filter(source__icontains=source_filter)
    quotes = quotes.order_by(sort_by)[:10]
    sources = Quote.objects.values_list('source', flat=True).distinct()
    return render(request, 'quotes/top_quotes.html', {'quotes': quotes, 'sources': sources, 'current_source': source_filter, 'sort_by': sort_by})