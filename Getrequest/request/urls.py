from django.urls import path
from .views import jsonview


urlpatterns = [
    path('jsonview/', jsonview, name='jsonview'),
]