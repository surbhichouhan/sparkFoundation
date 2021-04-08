from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField(max_length=150)
    current_balance = models.FloatField()
    

    def __str__(self):
        return self.name

class Transfer(models.Model):
    from_customer = models.CharField(max_length= 50)
    to_customer   = models.CharField(max_length = 50)
    balance_transferred = models.FloatField()

    def __str__(self):
        return self.from_customer+" to "+self.to_customer


