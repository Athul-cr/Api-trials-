from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Book(models.Model):
    book_name=models.CharField(max_length=120)
    price=models.IntegerField()
    author=models.CharField(max_length=120)
    createdby=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
    