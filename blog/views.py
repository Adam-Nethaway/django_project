from django.shortcuts import render

posts = [
    {
        'author': 'Adam',
        'title': "Blog Post 1",
        'content': "First post content",
        'date_posted': 'March 9, 2024'
    },
    {
        'author': 'John',
        'title': "Blog Post 2",
        'content': "Second post content",
        'date_posted': 'March 9, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})



