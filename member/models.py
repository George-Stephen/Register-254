from django.db import models
from cloudinary.models import CloudinaryField

class Member(models.Model):
    member_picture = CloudinaryField('image')
    id_number = models.CharField(max_length=255)
    member_number = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    date_birth = models.DateTimeField()
    phone_number = models.CharField(max_length=10)
    county = models.CharField(max_length=255)
    constituency = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return self.member_number

class Card(models.Model):
    card_prefix =  models.CharField(max_length=255)
    card_name = models.CharField(max_length=255)

    def __str__(self):
        return self.card_prefix

class Order(models.Model):
    card_type = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    order_agent = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.destination
