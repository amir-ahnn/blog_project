from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import NewPostFrom
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

def homepageview(request):
    return render(request, 'templates/home.html')

class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'post'


class PostCreatView(generic.CreateView):
    form_class = NewPostFrom
    template_name = 'blog/create_post.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostFrom
    template_name = 'blog/create_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_lists')

