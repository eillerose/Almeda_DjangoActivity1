from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This corresponds to the homepage
    path('/app1/page1/', views.page1, name='page1'),  # Add your routes here
    path('/app1/page2/', views.page2, name='page2'),
]
