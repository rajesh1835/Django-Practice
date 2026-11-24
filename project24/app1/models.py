from django.db import models


class Bank(models.Model):

    bank_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.bank_name

class Branch(models.Model):

    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=15, primary_key=True)
    branch = models.CharField(max_length=100)
    address = models.TextField()
    mobile = models.IntegerField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.branch

class BusinessEmployemntData(models.Model):
    series_reference = models.CharField(max_length=50)
    period = models.FloatField()
    data_value = models.CharField(max_length=30)
    suppressed = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50)
    units = models.CharField(max_length=50)
    magnitude = models.IntegerField()
    subject = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    series_title1 = models.CharField(max_length=100)
    series_title2 = models.CharField(max_length=100)

    def __str__(self):
        return self.series_reference