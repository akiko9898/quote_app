from django.urls import path
from .views import random_quote, add_quote, top_quotes

urlpatterns = [
    path('', random_quote, name='random_quote'),
    path('add/', add_quote, name='add_quote'),
    path('top/', top_quotes, name='top_quotes'),
]