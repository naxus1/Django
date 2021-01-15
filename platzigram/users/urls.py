"""user URLS"""

# Django
from django.urls import path
from django.views.generic import TemplateView

# Views
from users import views

urlpatterns = [

    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name="login"
    ),
    path(
        route='logout',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
         ),
]
