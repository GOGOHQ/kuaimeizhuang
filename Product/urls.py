from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.fetchProductList),
    path('<int:id>',views.fetchProduct)
]
