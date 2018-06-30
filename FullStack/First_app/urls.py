from django.urls import path
from First_app import views



urlpatterns= [
  path(r'',views.index,name='index'),
]
