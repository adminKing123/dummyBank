from email.policy import default
from django.db import models
from django.utils import timezone


class Total(models.Model):
    total = models.PositiveBigIntegerField(default=0)

# Create your models here.
class Record(models.Model):
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveBigIntegerField(null=False)
    D_CHOICES = (
        (True, 'Deposite'),
        (False, 'Withdrawl'),
    )
    is_deposited = models.BooleanField(choices=D_CHOICES)
    description = models.TextField(default="")
    
    class Meta:
        ordering = ['-transaction_date']