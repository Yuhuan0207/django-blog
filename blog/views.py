from django.shortcuts import render

posts = [
	{
		'author':'Katie',
		'title': 'post 1',
		'content': 'this is dummy post 1'
	},
	{
		'author':'Grace',
		'title': 'post 2',
		'content': 'this is dummy post 2'
	}	
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
