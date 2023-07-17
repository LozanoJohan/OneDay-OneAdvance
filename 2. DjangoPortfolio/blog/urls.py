from django.urls import path
from .views import post, post_detail


app_name = 'blog'

urlpatterns = [
    path('', post, name='post'),
    path('<int:post_id>/', post_detail, name='post_detail'),
]