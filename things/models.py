from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):  # bu yerda djangoni ozining userini ishlatyapmiz (AbstractUser) orqali
    full_name = models.CharField(max_length=256)
    Address = models.ManyToManyField("Address")


class Country_Region(models.Model):
    name = models.CharField(max_length=250)


class City(models.Model):
    name = models.CharField(max_length=200)


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=200, default=None)
    Zip_Code = models.IntegerField()
    country_region = models.ForeignKey(Country_Region, on_delete=models.CASCADE, null=True)


# Store'ni tovarlar kategoryasi
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


# Store'ni tovari (produkti)
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ManyToManyField("Image")
    size = models.ManyToManyField("Size")
    color = models.ManyToManyField("Color")
    price = models.FloatField(default=False)
    style = models.CharField(max_length=100)
    desc = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


# Store'ni tovarlarni rasimlari    
class Image(models.Model):
    photo = models.ImageField(default=False)


# Store'ni tovarlarni razmerlari
class Size(models.Model):
    number = models.FloatField(null=True)

    def __str__(self):
        return str(self.number)


# Store'ni tovarlarni ranglari
class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# Tovar haqida otziv uchun
class Review_product(models.Model):
    comment = models.CharField(max_length=256)
    image = models.ManyToManyField("Rw_pr_img")
    star = models.IntegerField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


# Otziv uchun rasm
class Rw_pr_img(models.Model):
    image = models.ImageField()


class UserCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="media/user/default.jpg")


###############################################################################################################


class NotificationType(models.Model):  # Уведомления типлари
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Notification(models.Model):  # Уведомления
    name = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=256, null=True)
    image = models.ImageField(null=True)
    NotificationType = models.ForeignKey(NotificationType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


#################################################################################################################


class Order(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=False)


###################################################################################################################
# Pay


class Transaction(models.Model):
    PROCESSING = 'processing'
    FINISHED = 'finished'
    CANCELED = 'canceled'
    STATUS = ((PROCESSING, PROCESSING), (FINISHED, FINISHED), (CANCELED, CANCELED))
    click_trans_id = models.CharField(max_length=255)
    merchant_trans_id = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    sign_string = models.CharField(max_length=255)
    sign_datetime = models.DateTimeField(max_length=255)
    status = models.CharField(max_length=25, choices=STATUS, default=PROCESSING)

    def __str__(self):
        return self.click_trans_id
