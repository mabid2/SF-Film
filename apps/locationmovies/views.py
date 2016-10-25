from django.shortcuts import render, redirect
from .models import Users, Movies, Favorites
import csv

def index(request):
    with open(r"C:\databasecsv.csv") as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        for row in reader:
            if row:
                for string in row:
                    if "Actor" not in string:
                        try:
                            movies = Movies()
                            movies.title = string[0]
                            movies.release_year = string[1]
                            movies.location = string[2]
                            movies.production_company = string[4]
                            movies.director = string[6]
                            movies.writer = string[7]
                            movies.actors = string[8] + " " + string[9] + " " + string[1]
                        except IndexError:
                            pass
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


def contact(request):
    return render(request, 'locationmovies/contact_us.html')