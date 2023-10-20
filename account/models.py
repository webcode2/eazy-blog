from django.db import models


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=205)


class Profile(models.Model):
    bio = models.TextField(max_length=500)
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='account_profile')

    def get_email(self):
        return self.user.email

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.get_email()