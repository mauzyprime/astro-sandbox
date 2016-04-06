from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Query, Dates
from .forms import QueryForm
from django.db import connection

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})
    
def about(request):
	return render(request, 'blog/about.html',{})

def query_new(request):
	if request.method == "POST":	
		form = QueryForm(request.POST)
		if form.is_valid():
			query = form.save(commit=False)
			query.save()
			return redirect('results', pk=query.pk)
			
	else:
		form = QueryForm()	
	return render(request, 'blog/query.html', {'form': form})
	
def results(request, pk):
	cursor = connection.cursor()
	cursor.execute('select id,Day from blog_dates;')
	results = cursor.fetchall()
	#resultsList = Dates.objects.all()
	for result in results:
		resultsList.append(result)
	
	
	return render(request, 'blog/results.html', {'resultsList':resultsList})

#end
	

	
