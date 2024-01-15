from django.db import models

# Create your models here.

class admin_reg(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=10)

class property(models.Model):
    image=models.FileField(upload_to='realestate_app/static')
    property_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    features=models.CharField(max_length=70)
    def __str__(self):
        return self.property_name

class rooms(models.Model):
    img=models.FileField(upload_to='realestate_app/static')
    choice=[
        ('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('3BHK','3BHK'),
        ('4BHK','4BHK'),
    ]
    type=models.CharField(max_length=50,choices=choice)
    room_no = models.CharField(max_length=10)
    cost=models.IntegerField()
    features=models.CharField(max_length=100)
    property_name=models.CharField(max_length=50)

    def __str__(self):
        return self.type

class tenent_profile(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    choice=[
        ('Aadhaar','Aadhaar'),
        ('Voterid','Voterid'),
    ]
    type=models.CharField(max_length=20,choices=choice)
    proof=models.FileField(upload_to='realestate_app/static')
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    date_of_arrival=models.DateField()
    property_name=models.CharField(max_length=50)
    property_type=models.CharField(max_length=50)
    room_no=models.CharField(max_length=20)

