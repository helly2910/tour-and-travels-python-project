from django.contrib import admin
from . models import Packages, Package_details, Booking, Contact, FeedBack

# Register your models here.
class Admin_Booking(admin.ModelAdmin):
	list_display = ['booking_user', 'booking_package', 'booking_phone', 'start_date', 'travellers']

admin.site.register(Packages)
admin.site.register(Package_details)
admin.site.register(Booking, Admin_Booking)
admin.site.register(Contact)
admin.site.register(FeedBack)