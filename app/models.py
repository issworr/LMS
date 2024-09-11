from django.db import models 
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=70)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, default= "")

    def __str__(self):
        return self.name
    

class Category(models.Model):
    BOOK_CATEGORIES = (
        ('Poetry' , 'Poetry'),
        ('Romance' , 'Romance'),
        ('Political thriller' , 'Political thriller'),
        ('Philosophy' , 'Philosophy'),
    )

    name = models.CharField(max_length=100, choices= BOOK_CATEGORIES)

    def __str__(self):
        return self.name  
    
class Book(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    file = models.FileField(upload_to= 'books/') 



    def __str__(self):
        return self.title
