from django.db import models

class assignment4app(models.Model):
    GENDER_CHOICES = [
        ('', 'Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name