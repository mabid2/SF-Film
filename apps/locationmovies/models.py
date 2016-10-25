from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
import datetime
now = datetime.datetime.now()
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def logUser(self, username_in, pwd_in):
        error = False
        print (username_in)
        if len(username_in) < 2:
            error = True  # END OF EMAIL VALIDATION

        if len(pwd_in) < 8:
            error = True  # END OF PASSWORD VALIDATION

        if error is True:
            return False
        else:
            passwordHash = Users.UserManager.filter(username=username_in).last().password.encode()
            if bcrypt.hashpw(pwd_in, passwordHash) == passwordHash:
                return True

    def regUser(self, username_up, email_up, pwd_up):
        error = False
        if len(username_up) < 2:
            error = True
        elif not (username_up.isalpha()):
            error = True  # END OF FIRST NAME VALIDATIONN

        if not EMAIL_REGEX.match(email_up):
            error = True  # END OF EMAIL VALIDATION

        if len(pwd_up) < 8:
            error = True  # END OF PASSWORD VALIDATION

        if error is True:
            return False
        else:
            hashedPW = bcrypt.hashpw(pwd_up, bcrypt.gensalt())
            Users.UserManager.create(username=username_up, email=email_up, password=hashedPW, created_at=now)
            return True


class Movies(models.Model):
    title = models.CharField(max_length=60)
    release_year = models.CharField(max_length=4)
    location = models.CharField(max_length=100)
    production_company = models.CharField(max_length=40)
    director = models.CharField(max_length=40)
    writer = models.CharField(max_length=40)
    actors = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favorites(models.Model):
    location = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Users(models.Model):
    username = models.CharField(max_length=60)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorite_id = models.ManyToManyField(Favorites)
    UserManager = UserManager()


