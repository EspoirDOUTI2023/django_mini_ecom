from django.urls import path
from .views import index, product_detail, checkout, confirmation

urlpatterns = [
    path('', index, name='home'),
    path('product/<str:id>', product_detail, name='product_detail'),
    path('checkout/', checkout, name='checkout'),
    path('confirmation/', confirmation, name='confirmation')

]