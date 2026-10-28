from django.db import models


class Expense(models.Model):
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.description
