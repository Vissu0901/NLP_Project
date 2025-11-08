from django.urls import path
from . import views

urlpatterns = [
    # Add your API endpoints here
    path('', views.api_root, name='api-root'),
]
