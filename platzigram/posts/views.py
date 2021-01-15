""" Post views """
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Forms

from posts.forms import PostForm

# Models
from posts.models import Post


# @login_required
# def list_posts(request):
#     """ List Existing posts """
#     posts = Post.objects.all().order_by('created')
#     return render(request, 'posts/feed.html', {'posts': posts})


class PostFeedView(LoginRequiredMixin, ListView):
    """List all publish post"""
    template_name = 'posts/feed.html'
    model = Post
    ordering = '-created'
    paginate_by = 2
    context_object_name = 'posts'


class DetailPostView(LoginRequiredMixin, DetailView):
    """Show detail post"""
    template_name = 'posts/detailpost.html'
    model = Post
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """create new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


# @login_required()
# def create_post(request):
#     """create new post"""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('post:feed')
#     else:
#         form = PostForm()
#     return render(
#         request,
#         'posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )
