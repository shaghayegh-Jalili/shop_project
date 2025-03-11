from django.urls import path
from .views import myIndex

urlpatterns = [
    path('', myIndex, name='myIndex'),
]