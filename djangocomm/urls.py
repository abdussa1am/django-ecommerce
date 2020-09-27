from django.urls import path
from . views import Home , add_to_cart , remove_from_cart , SearchResultsView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]