from django.db import models

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone= models.CharField(max_length=50)
    date = models.DateTimeField()
    room = models.CharField(
        max_length=100,
        default='Standard Room'  # Default value for new reservations
    )
    message = models.CharField(max_length=500)



    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name




class  Manager(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


