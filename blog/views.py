from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, Team, Comment
from .forms import PostForm, CommentForm, UserForm 
from django.urls import reverse_lazy
 

def index(request):
    members = Team.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'index.html', context=context)


def signup(request):
    context = {
        'form': UserForm()
    }
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('login',)
        
    return render(request, 'sign_up.html', context=context)


def contact(request):
    return render(request, 'contact.html')


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')


class PostDetailView(DetailView):
    model = Post    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = Comment.objects.all().order_by('-created_at')
        return context
    


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'stories'
    
    model = Post
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'post-detail'

    model = Post
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('stories')


############################################################

##############################################################

@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post-detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', context={'form': form, })


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)


@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post-detail', pk=post_pk)


@login_required
def stories(request):
    posts = Post.objects.all()
    pub_posts = Post.objects.filter(
        publish_date__lte=timezone.now()).order_by('publish_date')
    drafts = Post.objects.filter(
        publish_date__isnull=True).order_by('create_date')
    context = {
        'published': pub_posts,
        'drafts': drafts,
        'posts': posts,
    }
    return render(request, 'stories.html', context=context)
