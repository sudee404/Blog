from django.shortcuts import render
from django.views import generic
from .models import Post,Author,Tags,Team
# Create your views here.
def index(request):
    members = Team.objects.all()
    context = {
        'members':members,
    }
    return render(request,'index.html',context=context)

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

class BlogCreateView(generic.CreateView):
    model = Post
    fields = ('title','content','image')
    
class BlogDetailView(generic.DetailView):
    model = Post
    
class BlogListView(generic.ListView):
    model = Post