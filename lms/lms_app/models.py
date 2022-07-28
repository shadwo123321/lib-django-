from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Books(models.Model):

   

    title = models.CharField(max_length=50, null=True,blank=True)
    author = models.CharField(max_length= 50)
    photo_book = models.ImageField(upload_to ='photos')
    photo_author = models.ImageField(upload_to = 'photos')
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2 , null=True , blank= True)
    rental_price_day = models.DecimalField(max_digits=5 , decimal_places=2, null=True , blank= True)
    period_rental = models.IntegerField(null=True, blank=True)
    rental_total =models.DecimalField(max_digits=5 , decimal_places=2, null=True , blank= True)
    active = models.BooleanField(default=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title