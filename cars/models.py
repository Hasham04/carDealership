from django.db import models
from datetime import datetime
from salesman.models import Salesman


class Car(models.Model):
	salesman = models.ForeignKey(Salesman, on_delete= models.DO_NOTHING)
	title = models.CharField(max_length=200)
	address = models.TextField(blank=True)
	make=models.CharField(max_length=200)
	bodyType=models.CharField(max_length=200)
	mileage= models.IntegerField()
	description = models.TextField(blank=True)
	price = models.IntegerField()
	transmission = models.CharField(max_length=200)
	driveTrain =models.CharField(max_length=200)
	engineType = models.CharField(max_length=200)
	exteriorColor=models.CharField(max_length=200)
	interiorColor=models.CharField(max_length=200)
	doors=models.IntegerField()
	vin=models.CharField(max_length=200)
	vehicleID=models.IntegerField()
	photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
	photo1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
	photo2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
	photo3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
	photo4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
	photo5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
	photo6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
	is_published = models.BooleanField(default=True)
	list_date = models.DateTimeField(default=datetime.now,blank=True)


	def __str__(self):
		return self.title