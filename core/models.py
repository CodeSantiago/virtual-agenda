from django.db import models

# Create your models here.

class Contact(models.Model):
    avatar = models.ImageField(null=True, blank=True, upload_to='contact')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank= True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name