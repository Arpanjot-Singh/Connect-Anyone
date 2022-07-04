from django.urls import path
from search.views import Search

urlpatterns = [
    path('',Search,name='search'),
    ]