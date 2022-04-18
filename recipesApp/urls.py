from django.urls import path

from recipesApp.views import home

urlpatterns = [
    path('', home),
]
