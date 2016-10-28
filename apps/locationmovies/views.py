from django.shortcuts import render, redirect
from .models import Users, Movies, Favorites
from django.contrib import messages
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
    info = Users.UserManager.regUser(username, email, password)
    if info[0] is True:
        request.session['name'] = username

        return render(request, 'locationmovies/index.html')
    else:
        messages.error(request, 'Email is not valid', extra_tags='email')
        messages.error(request, 'Username is not long enough!!', extra_tags='username')
        messages.error(request, 'Password must be at least 8 characters!!', extra_tags='password')
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
        print 'Failed Login'
        context = {
            "invalid_reg": "Your credentials doesn't work!"
        }
        return render(request, 'locationmovies/login.html', context)


def logout(request):
   request.session.clear()
   return redirect('/')


def display(request, id):
    print "IN the display function"
    request.session['current_row'] = id
    row = Movies.objects.filter(id=id)[0]
    context = {
        'title': row.title,
        'release_year': row.release_year,
        'location': row.location,
        'director': row.director,
        'actor': row.actors

    }

    # x = row.location.split(' ')
    # print ('+'.join(x), "***************************")
    # context = {
    #     'movies': Movies.objects.all()
    # }
    return render(request, 'locationmovies/content.html', context)


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


def addWishlist(request, idObject):
    newEntry = Favorites()
    newEntry.save()
    newEntry.objects.create(movie_id=idObject)
    newEntry.save()
    print newEntry
    return redirect('/')

