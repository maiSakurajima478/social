from django.urls import path

from .views import (
    posts_view,
    profile_user_view,
    like,
)

app_name = 'blog'

urlpatterns = [
    path('', posts_view, name='posts'),
    path('profile/<int:pk>/', profile_user_view, name="profile"),
    
    path('like/<int:pk>', like, name='like')
]
