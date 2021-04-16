from django.db import models

# Create your models here.

class SiteModel(models.Model):
    name = models.CharField(max_length=255,unique=True)
    image = models.ImageField()
    price_function = models.TextField()

    def __str__(self):
        return self.name.capitalize()

class EntryModel(models.Model):
    site = models.ForeignKey(SiteModel,on_delete=models.CASCADE)
    url = models.CharField(max_length=10000)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} | {self.site.name}"

class OldEntryModel(models.Model):
    site = models.ForeignKey(SiteModel,on_delete=models.CASCADE)
    url = models.CharField(max_length=10000)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} | {self.site.name}"