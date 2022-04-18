from django.urls import path

from recipesApp.views import about, contact, home

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
]
