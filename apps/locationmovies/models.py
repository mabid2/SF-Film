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
        if len(username_in) < 2:
            error = True  # END OF EMAIL VALIDATION

        if len(pwd_in) < 8:
            error = True  # END OF PASSWORD VALIDATION

        if error is True:
            return False
        else:
            passwordHash = Users.UserManager.get(username=username_in).password.encode()
            if bcrypt.hashpw(pwd_in, passwordHash) == passwordHash:
                return True
            else:
                return False

    def regUser(self, username_up, email_up, pwd_up):
        error = []
        if len(username_up) < 2:
            # messages.error.extra_tags = 'username'
            error.append("Too short!! Username should be at least 2 characters")
        elif not username_up:
            error.append("Username field must be filled out")  # END OF FIRST NAME VALIDATION

        if not EMAIL_REGEX.match(email_up):
            error.append("Email is in wrong format")  # END OF EMAIL VALIDATION

        if len(pwd_up) < 8:
            error.append('Password is too short')
            # if pwd_up != passwordconf_up:
            # END OF PASSWORD VALIDATION
        if len(error) > 0:
            return [False, error]
        else:
            hashedPW = bcrypt.hashpw(pwd_up, bcrypt.gensalt())
            newuser = Users.UserManager.create(username=username_up, email=email_up, password=hashedPW, created_at=now)
            return [True]

    def validuser(self, username_valid):
        if len(username_valid) < 3:
            return True
        else:
            return False

    def validemail(self, email_valid):
        if not EMAIL_REGEX.match(email_valid):
            return True
        else:
            return False

    def validpassword(self, pass_valid):
        if len(pass_valid) < 9:
            return True
        else:
            return False

    def matchpasswords(self, password, confirmpass):
        if password != confirmpass:
            return True
        else:
            return False

class MoviesManager(models.Manager):
    def addMovie(self):
        return True


class Users(models.Model):
    username = models.CharField(max_length=60)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    UserManager = UserManager()


class Movies(models.Model):
    title = models.CharField(max_length=60, null=True)
    release_year = models.CharField(max_length=4, null=True)
    location = models.CharField(max_length=100, null=True)
    production_company = models.CharField(max_length=40, null=True)
    director = models.CharField(max_length=40, null=True)
    writer = models.CharField(max_length=40, null=True)
    actors = models.CharField(max_length=60, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorited_by = models.ManyToManyField(Users)
    MoviesManager = MoviesManager()

    def __unicode__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
        self.title, self.release_year, self.location, self.production_company, self.director, self.writer, self.actors)

    class Meta:
        ordering = ['title']