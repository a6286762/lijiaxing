from django.db import models
# -*- coding:utf-8 -*-
# Create your models here.
#class Publisher(models.Model):
#    name = models.CharField(max_length=30)
#    address = models.CharField(max_length=50)
#    city = models.CharField(max_length=60)
#    state_province = models.CharField(max_length=30)
#    country = models.CharField(max_length=50)
#    website = models.URLField()
    
class Author(models.Model):
#    AuthorID = models.CharField(max_length=30,primary_key=True)
    Name = models.CharField(max_length=40)
    Age = models.IntegerField(max_length=100)
    Country = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.Name
    
class Book(models.Model):
    ISBN = models.CharField(max_length=100,primary_key=True)
    Title = models.CharField(max_length=100)
    authorid = models.ManyToManyField(Author)
    Publisher = models.CharField(max_length=100)
    Publication_date = models.DateField()
    Price = models.FloatField(max_length=100)
    
    def __unicode__(self):
        return self.Title