from django.db import models

# Create your models here.

class Coreservices(models.Model):
    servicetype = models.CharField(max_length=100)
    servicereg = models.CharField(max_length=100)
    serviceicon = models.CharField(max_length=100)
    serviceiconsize = models.CharField(max_length=100)
    serviceiconcolor = models.CharField(max_length=100)
    serviceavialablty = models.CharField(max_length=100)
    cardcolor = models.CharField(max_length=100)
    btncolor = models.CharField(max_length=100)
    targetservice = models.CharField(max_length=100)


    def __str__(self):
        return self.servicetype
    
class Logo(models.Model):
    logo = models.ImageField(upload_to="logo")

    def __str__(self):
        return self.logo.name

class Document_img(models.Model):
    doc_img = models.ImageField(upload_to="image")

class Staff(models.Model):
    name = models.CharField(max_length=100)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    service_type = models.CharField(max_length=100)
    application_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    assign = models.ForeignKey(
        Staff,
        on_delete = models.SET_NULL,
        null = True
    )
    status = models.CharField(
        max_length=20,
        default="pending"
    )

    def __str__(self):
        return self.service_type
    

