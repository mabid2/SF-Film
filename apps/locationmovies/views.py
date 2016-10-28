from django.shortcuts import render, redirect
from .models import Users, Movies
from django.contrib import messages
import csv


def index(request):

    context = {
        "movies": Movies.MoviesManager.all()
    }

    return render(request, 'locationmovies/index.html', context)


def login(request):
    return render(request, 'locationmovies/login.html')



def registerUser(request):
    print "Hello!"
    username = request.POST.get("username_up")
    email = request.POST.get("email_up")
    password = request.POST.get("pwd_up").encode()
    confirmpassword = request.POST.get("passwordconf_up").encode()
    info = Users.UserManager.regUser(username, email, password)
    if info[0] is True:
        request.session['name'] = username

        return render(request, 'locationmovies/index.html')
    else:
        if Users.UserManager.validuser(username):
            messages.error(request, 'Username is not long enough!!', extra_tags='username')

        if Users.UserManager.validemail(email):
            messages.error(request, 'Email is not valid', extra_tags='email')

        if Users.UserManager.validemail(password):
            messages.error(request, 'Password must be at least 8 characters!!', extra_tags='password')

        if Users.UserManager.matchpasswords(password, confirmpassword):
            messages.error(request, 'Password Confirmation doesn\'t match!!', extra_tags='passwordconfirm')
        return redirect('/login')


def loginUser(request):
    username = request.POST.get("username_in")
    password = request.POST.get('pwd_in').encode()
    Users.UserManager.logUser(username, password)

    if Users.UserManager.logUser(username, password):
        request.session['name']= request.POST['username_in']

        print "Successful Login"
        print Users.UserManager.logUser(username, password)
        context = {
            "name": Users.UserManager.filter(username=username, password=password).last(),
            "message": "registered"
        }
        return redirect('/', context)
    else:
        if Users.UserManager.validuser(username):
            messages.error(request, 'Username is not long enough!!', extra_tags='username_in')
        if Users.UserManager.validemail(password):
            messages.error(request, 'Password must be at least 8 characters!!', extra_tags='password_in')

        return redirect('/login')


def logout(request):
    request.session.clear()
    return redirect('/')


def display(request, id):
    print "IN the display function"
    request.session['current_row'] = id
    row = Movies.MoviesManager.filter(id=id)[0]
    context = {
        'title': row.title,
        'release_year': row.release_year,
        'location': row.location,
        'director': row.director,
        'actor': row.actors

    }

    return render(request, 'locationmovies/content.html', context)


def displayAll(request):
    context = {
        # 'movies': Movies.objects.raw('SELECT * from Movies')
        'movies': Movies.MoviesManager.all()
    }
    return render(request, 'locationmovies/list.html', context)


def search(request):
    if request.method == 'POST':
        queryr = request.POST.get('search')
        result = Movies.MoviesManager.filter(title__contains=queryr).first()
        print result

    context = {
        "movies": result
    }
    return render(request, 'locationmovies/searchResult.html', context)


def contact(request):
    return render(request, 'locationmovies/contact_us.html')



def deleteWishlist(request):
    if request.session["name"]:
        # print("VAGINA: {}".format(request.session['name']))
        userGuy = Users.UserManager.get(username=request.session["name"])
        delete = request.POST.get("deleteMe")
        print delete
        # newFav = Movies.MoviesManager.get(id=delete)
        #
        # newFav.favorited_by.remove()
        context = {"favorites": userGuy.movies_set.all()}

        return render(request, 'locationmovies/wishlist.html', context)
    else:
        return redirect('/displayAll')

def displayapes(request):
   return render(request, 'locationmovies/displayapes.html')


def displaysan(request):
   return render(request, 'locationmovies/displaysan.html')

def displayharry(request):
   return render(request, 'locationmovies/displayharry.html')

def displayvertigo(request):
   return render(request, 'locationmovies/displayvertigo.html')


def wishlist(request):
    if request.session["name"]:
        userGuy = Users.UserManager.get(username=request.session["name"])

        if request.POST and request.POST.get("addMe"):
            movieId = request.POST.get("addMe")
            newFav = Movies.MoviesManager.get(id=movieId)
            newFav.favorited_by.add(userGuy)
        elif request.POST and request.POST.get("deleteMe"):
            movieId = request.POST.get("deleteMe")
            newFav = Movies.MoviesManager.get(id=movieId)
            newFav.favorited_by.remove(userGuy)


        context = {"favorites": userGuy.movies_set.all()}

        return render(request, 'locationmovies/wishlist.html', context)
