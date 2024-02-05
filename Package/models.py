from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Packages(models.Model):
	p_id = models.AutoField(primary_key=True)
	package = models.CharField(max_length=100)
	p_image = models.ImageField(upload_to='Package/images')
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.package

class Package_details(models.Model):
	p_id = models.AutoField(primary_key=True)
	p_title = models.CharField(max_length=80)
	p_price_per_person = models.IntegerField()
	p_package = models.ForeignKey(Packages, on_delete=models.CASCADE)
	p_package_days = models.CharField(max_length=50)
	p_travel_through = models.CharField(max_length=100)
	p_phone = models.IntegerField()
	p_provider_name = models.CharField(max_length=50)
	p_provider_address = models.CharField(max_length=120)
	p_full_package_description = models.TextField(max_length=255)
	p_package_image = models.ImageField(upload_to='Package/images')

	def __str__(self):
		return self.p_title


class Booking(models.Model):
	booking_id = models.AutoField(primary_key=True)
	booking_user = models.ForeignKey(User, on_delete=models.CASCADE)
	booking_package = models.ForeignKey(Package_details, on_delete=models.CASCADE)
	booking_address = models.CharField(max_length=255)
	booking_phone = models.IntegerField()
	boarding = models.CharField(max_length=50)
	start_date = models.DateField()
	travellers = models.IntegerField()
	room_wise = models.CharField(max_length=50)


class Contact(models.Model):
	c_id = models.AutoField(primary_key=True)
	c_name = models.CharField(max_length=40)
	c_email = models.EmailField(max_length=70)
	c_phone = models.IntegerField()
	c_msg = models.CharField(max_length=255)

	def __str__(self):
		return self.c_name

class FeedBack(models.Model):
	f_id = models.AutoField(primary_key=True)
	f_user = models.ForeignKey(User, on_delete=models.CASCADE)
	f_msg = models.TextField(max_length=255)

	def __str__(self):
		return self.f_user.first_name