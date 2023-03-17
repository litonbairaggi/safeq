from django.db import models

# Create your models here.

class Setting(models.Model):
    email = models.CharField(max_length=100, unique=True, blank=False)
    working_time = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=100, unique=True, blank=False)
    facebook = models.URLField(max_length=100, unique=True, blank=False)
    twitter = models.URLField(max_length=100, unique=True, blank=False)
    instagram = models.URLField(max_length=100, unique=True, blank=False)
    linkedin = models.URLField(max_length=100, unique=True, blank=False)
    weblink = models.URLField(max_length=100, unique=True, blank=False)
    logo_img = models.ImageField(upload_to='settings/',blank=False)
    descriptions = models.TextField(max_length=700, blank=True, null=True)
    
    # trip_number = models.URLField(("Trip Number"), max_length=128, db_index=True, unique=True, blank=True)

    def save(self):
        # count will have all of the objects from the Seeting model
        count = Setting.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = Setting.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 1:
            super(Setting, self).save()
        elif save_permission:
            super(Setting, self).save()

    def has_add_permission(self):
        return Setting.objects.filter(id=self.id).exists()