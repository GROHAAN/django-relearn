from django.shortcuts import render

# Create your views here.

def home (req):
    data={
        'age': 25
    }
    return render(req, 'home.html', data)

def about (req):
    data={
        'students': ['abhishek', 'rohaan', 'virat','rohit']
    }
    return render(req, 'about.html', data)