from django.db import models

# Create your models here.
class Sketch(models.Model):
    img=models.ImageField(upload_to='pics')

class Handcraft(models.Model):
    img=models.ImageField(upload_to='picsofhandcraft')

class Plant(models.Model):
    img=models.ImageField(upload_to='picsofplant')

class Card(models.Model):
    img=models.ImageField(upload_to='picsofcard')

class Human(models.Model):
    img=models.ImageField(upload_to='picsofhuman')

class Building(models.Model):
    img=models.ImageField(upload_to='picsofbuilding')

class Nature(models.Model):
    img=models.ImageField(upload_to='picsofnature')
