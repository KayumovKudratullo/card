from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return  self.name
    
    class Meta:
        ordering = 'name',
        verbose_name_plural = 'Korxonalar'
        vorbose_name = 'Korxona'

class Order(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    text = models.TextField()
    is_chacked = models.BooleanField(default=False)