from django.db import models

class Mamber(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    dob = models.DateField()
    GENDER = (
    ('0', 'Male'),
    ('1', 'Female'),
    ('3', 'Other'),
    )
    gender = models.CharField(max_length=1,choices=GENDER)
    CONTRIBUTED = (
    ('0', 'Yes'),
    ('1', 'No'),
    )
    contributed = models.CharField(max_length=1,default='1',choices=CONTRIBUTED) #Will remove when we get content for homepage till we gonna display users who contributed this projects (iff class mambers)

    def __str__ (self):
        return self.name

# Create your models here.
# class Class(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=20, unique=True)
#     dob = models.DateField()
#     GENDER = (
#     ('0', 'Male'),
#     ('1', 'Female'),
#     ('3', 'Other'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER)
#
#     def __str__ (self):
#         return self.name
