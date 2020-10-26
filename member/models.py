from django.db import models

class Member(models.Model):
    id_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=10)
    county = models.CharField(max_length=255)
    sub_county = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Order(models.Model):
    number_of_cards = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    ordered_by = models.CharField(max_length=255)

    def __str__(self):
        return self.destination
