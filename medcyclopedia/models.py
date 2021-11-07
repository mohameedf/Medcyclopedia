from django.db import models

# Create your models here.
# creste a model for  drugs and their properties


class Drug(models.Model):
    name = models.CharField(max_length=200)
    genericName = models.CharField(max_length=200)
    brandName = models.CharField(max_length=200)
    federalSchedule = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    img = models.ImageField(upload_to='drugs/', blank=True)
    description = models.TextField()
    primaryIndications = models.CharField(max_length=400)
    # tags
    drugClass = models.ManyToManyField(
        'DrugClass', blank=True, related_name='drugs')

    def __str__(self):
        return self.name


class Tag(models.Model):
    drugs = models.ManyToManyField(Drug, blank=True, related_name='Drugs')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DrugClass(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='drugs/', blank=True)
    # drugs

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='drugs/', blank=True)
    # articles

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(upload_to='drugs/', blank=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='articles')
    author = models.ForeignKey(
        'rest_auth.EmailAccount', on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category, related_name='articles')

    def __str__(self):
        return self.title
