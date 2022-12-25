from django.db import models

# Create your models here.

# Create your models here.
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'Registrations'

class UserSearchUrlModel(models.Model):
    id = models.AutoField(primary_key=True)
    urlname = models.CharField(max_length=250)
    depthfecth = models.IntegerField()
    c_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.urlname
    class Meta:
        db_table = "UserSearchUrls"

class CSRFResponse(models.Model):
    id = models.AutoField(primary_key=True)
    regex = models.CharField(max_length=10000)
    matches = models.CharField(max_length=100000)
    urlname = models.CharField(max_length=1000)
    c_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.urlname
    class Meta:
        db_table = "csrftables"

