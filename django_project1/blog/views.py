from django.shortcuts import render

posts = [
    {
        'author': 'kevin',
        'title': 'blog post 1',
        'content': 'First post contnet',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'john doe',
        'title': 'blog post 2',
        'content': 'second post contnet',
        'date_posted': 'August 29, 2018'
    }
]

# Create your views here. How we want to handle routes.
def home(request):
        context = {
            'posts': posts
        }
        return render(request, 'blog/home.html', context)

def about(request):
        return render(request, 'blog/about.html', {'title': "About"})






