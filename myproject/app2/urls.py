from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This corresponds to the homepage
    path('page1/', views.page1, name='page1'),  # Add your routes here
    path('page2/', views.page2, name='page2'),
]
