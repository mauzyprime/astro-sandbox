from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Query
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
	#THING = str(get_object_or_404(Query,pk=pk))
	row = cursor.execute('select * from information_schema.tables;')
	#result = query
	result = cursor.fetchall()
	
	x = cursor.description
	resultsList = []
	for r in results:
		i = 0
		d = {}
		while i < len(x):
			d[x[i][0]] = r[i]
			i = i+1
		resultsList.append(d)
	return render(request, 'blog/results.html', {'result':resultsList})

#end
	

	
