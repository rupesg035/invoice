from django.urls import path
from . import views

urlpatterns = [    
    path('invoice/create/', views.create),
    path('invoice/update/', views.update),
    path('invoice/delete/', views.delete),
    path('invoice/retrieve/', views.retrieve),

]