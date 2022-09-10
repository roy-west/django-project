from django.urls import path
from .views import post_list_view, post_detail_view, post_search_view

urlpatterns = [
    path('', post_list_view),
    path('posts/', post_search_view),
    path('posts/<int:id>/', post_detail_view),
]