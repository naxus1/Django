"""Posts URLS"""

# Django
from django.urls import path

# views
from posts import views


urlpatterns = [
    path(
        route='',
        view=views.PostFeedView.as_view(),
        name="feed"
    ),

    path(
        route='new/',
        view=views.CreatePostView.as_view(),
        name="create_post"
         ),

    path(
        route='detail/<int:pk>/',
        view=views.DetailPostView.as_view(),
        name='detail_post'
         ),
]
