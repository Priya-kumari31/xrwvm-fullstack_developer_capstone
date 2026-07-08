from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default="")
    year = models.IntegerField(default=2023)

    def __str__(self):
        return self.name


class Dealer(models.Model):
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=200, default="")
    zip = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.full_name


class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    review = models.TextField()
    car_make = models.CharField(max_length=100, default="")
    car_model = models.CharField(max_length=100, default="")
    car_year = models.IntegerField(default=2023)
    sentiment = models.CharField(max_length=50, default="neutral")

    def __str__(self):
        return self.review
