""" Platzigram middleware """

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware

    Ensure every user that is interacting with the platform
    have their profile picture an biography.
    """
    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            profile = request.user.profile
            print(profile.picture)
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('users:update_profile'), reverse('users:logout')] and not request.path.startswith(
                        '/admin/'):
                    return redirect('users:update_profile')

        response = self.get_response(request)
        return response
