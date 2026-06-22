from django.db import models

class Mahsulot(models.Model):

    KATEGORIYA_CHOICES = [
        ('fruits', 'Fruits & Veges'),
        ('juices', 'Juices'),
        ('bolalar', 'Bolalar Uchun'),
        ('aksiyalar', 'Haftalik Aksiyalar'),
    ]

    nom = models.CharField(max_length=100)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    rasm = models.ImageField(upload_to='products/')
    tavsif = models.TextField()
    

    kategoriya = models.CharField(
        max_length=50, 
        choices=KATEGORIYA_CHOICES, 
        default='fruits'
    )

    def __str__(self):
        return self.nom