from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('all_customers', views.all_customers),
    path('customer/<int:id>', views.customer),
    path('<int:from_id>/all_customers',views.transfer),
    path('<int:from_id>/customer/<int:to_id>',views.money_transfer),
    path('done', views.done),
]