from django.urls import path
from .views import main_page, test_view

urlpatterns = [
    path('', main_page),
    path('test/', test_view)
]