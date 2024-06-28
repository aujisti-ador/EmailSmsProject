from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField()
    address = models.TextField(blank=True)  # Making address optional

    def __str__(self):
        return self.name
