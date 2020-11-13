from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
from services.utils import create_new_ref_number
# Create your models here.

class Userprofile(models.Model):
    email = models.EmailField(max_length=100, primary_key=True,default="")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    image = models.ImageField(default='services/images/default.jpg', upload_to='services/profile_pics')
    profession = models.CharField(max_length=200)
    bio = models.TextField()
    def __str__(self):
        return self.firstname

class Category(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    icon = models.ImageField(upload_to='services/images',default="")
    desc = models.TextField(default=" ")
    def __str__(self):
        return self.name

class Tutorial(models.Model):
    title = models.CharField(max_length=100,primary_key=True)
    desc =  models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catego = models.ForeignKey(Category, on_delete=models.CASCADE)
    videofile= models.FileField(upload_to='services/videos',null=True)
    imagefile = models.ImageField(upload_to='services/images',default="")
    price = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
    approval = models.NullBooleanField()
    
    def __str__(self):
        return self.title

class Purchase(models.Model):

    Referrence_Number = models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           primary_key=True,
           default=create_new_ref_number()
      )
    fullname = models.CharField(max_length=50, default=" ")
    customuser = models.ForeignKey(User, on_delete=models.CASCADE)
    tuto = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    purchasedate = models.DateTimeField(default=timezone.now)


    # def __str__(self):
    #     return self.customuser

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email_ad = models.EmailField(default='NULL')
    message= models.TextField("Message",default=" ")
    def __str__(self):
        return self.first_name + ' ' + self.last_name
