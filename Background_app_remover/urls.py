
from django.urls import path
from .views import remove_background, Home

urlpatterns = [
    path("", Home, name="Home"),
    path('remove_bg/', remove_background, name='remove_background'),
    
]
