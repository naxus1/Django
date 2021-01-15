"""
User views
"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

# Forms
from users.forms import SignupForm

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    """User Detail view"""
    template_name = 'users/detail.html'
    #queryset = User.objects.all()
    slug_url_kwarg = 'username'
    slug_field = 'username'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth_views.LoginView):
    """User login"""
    template_name = 'users/login.html'

# def login_view(request):
#     """ User Login """
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'invalid password'})
#     return render(request, 'users/login.html')


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Updated users profile """
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user`s profile"""
        print("self", self.request.user.profile)
        return self.request.user.profile

    def get_success_url(self):
        """Return to user`s profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


# @login_required()
# def update_profile(request):
#     """ Updated users profile """
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()
#             url = reverse('users:detail', kwargs={'username': request.user.username})
#             return redirect(url)
#     else:
#         form = ProfileForm()
#
#     return render(request,
#                   'users/update_profile.html',
#                   context={
#                       'profile': profile,
#                       'user': request.user,
#                       'form': form,
#                   })


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


# def signup(request):
#     """ User Sing up View"""
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = SignupForm()
#
#     return render(request, 'users/signup.html', context={'form': form})


@login_required
def logout_view(request):
    """ user logout """
    logout(request)
    return redirect('users:login')
