from django.urls import path
from .views import place_order, portfolio_value

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('portfolio_value/', portfolio_value, name='portfolio_value'),
]