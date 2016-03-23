from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import HomeForm


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})
    
#def return_result(request):
	#return render(request, 'blog/return_result.html',{})
	
