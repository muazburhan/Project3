from django.urls import path, include
from django.views.generic import ListView, DetailView
from .views import ItemCreateView
from . import views
from market.models import Item

urlpatterns = [
    path('', ListView.as_view(queryset=Item.objects.all().order_by("-date")[:25],template_name="market/home.html"), name='homepage'),
    path('<int:pk>', DetailView.as_view(model=Item, template_name="market/item.html"),name = 'item-detail'),
    path('item/add/',ItemCreateView.as_view(), name='item-create'),
]
