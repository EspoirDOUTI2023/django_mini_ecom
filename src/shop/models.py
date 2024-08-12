from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here. 
class Category(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    


class Order(models.Model):
    items = models.TextField()
    name = models.CharField(max_length=300)
    email = models.EmailField()
    amount = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)

    #order by date desc
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
