from django.db import models

# Create your models here.

class OurClient(models.Model):
    clients_img = models.ImageField(upload_to='our_client/',blank=False)