from django.db import models


class Savenow(models.Model):
    name = models.CharField(max_length=200, default=False, null=True)
    amount = models.DecimalField(max_digits=20,decimal_places=5, default=False, null=True)
    purpose = models.CharField(max_length=200, default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    

class Myplan(models.Model):
    name = models.CharField(max_length=200, default=False, null=True)
    amount = models.DecimalField(max_digits=20,decimal_places=5, default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
