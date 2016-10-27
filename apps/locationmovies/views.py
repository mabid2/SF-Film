from django.shortcuts import render, redirect
from .models import Users, Movies, Favorites
from django.db.models import Count
import csv


def index(request):
    context = {
        "movies": Movies.objects.all()
    }

    return render(request, 'locationmovies/index.html', context)


def login(request):
    return render(request, 'locationmovies/login.html')


def registerUser(request):
    print "Hello!"
    username = request.POST.get("username_up")
    email = request.POST.get("email_up")
    password = request.POST.get("pwd_up").encode()
    Users.UserManager.regUser(username, email, password)
    if Users.UserManager.regUser(username, email, password):
        context = {
            "name": username
        }
        return render(request, 'locationmovies/index.html', context)
    else:
        context = {
            "invalid_reg": "Your data is in the wrong format! Please check your spelling!"
        }
        return render(request, 'locationmovies/index.html', context)


def loginUser(request):
    username = request.POST.get("username_in")
    password = request.POST.get('pwd_in').encode()
    Users.UserManager.logUser(username, password)
    if Users.UserManager.logUser(username, password):
        context = {
            "name": Users.UserManager.filter(username=username).last(),
            "message": "registered"
        }
        return render(request, 'locationmovies/index.html', context)
    else:
        context = {
            "invalid_reg": "Your credentials doesn't work!"
        }
        return render(request, 'locationmovies/index.html', context)



def display(request):
    return render(request, 'locationmovies/content.html')


def displayAll(request):
    context = {
        # 'movies': Movies.objects.raw('SELECT * from Movies')
        'movies': Movies.objects.all()
    }
    return render(request, 'locationmovies/list.html', context)


def search(request):
    if request.method == 'POST':
        queryr = request.POST.get('search')
        result = Movies.objects.filter(title__contains=queryr).first()
        print result

    context = {
        "movies": result
    }
    return render(request, 'locationmovies/searchResult.html', context)


def contact(request):
    return render(request, 'locationmovies/contact_us.html')


# def addWishlist(request):
#
#     return redirect('/')