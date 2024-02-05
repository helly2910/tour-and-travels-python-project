from django.contrib import admin
from django.urls import path
from . import views


# django admin customization

admin.site.site_header = "Holiday Package Admin"
admin.site.site_title = "Holiday Package Admin Portal"
admin.site.index_title = "Welcome to Holiday Package Admin."

urlpatterns = [
    path('', views.index, name="Indexpage"),
    path('destinations/', views.packages, name="Services"),
    path('signup/', views.handlesignup, name='signup'),
    path('login/', views.handlesignin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
    path('home/', views.home, name="Homepage"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('service/', views.whyus, name="service"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('subpackage/<mypackage>/', views.subpackage, name="Subpackages"),
    path('checkout/<int:myid>/', views.checkout, name="checkoutPackage"),
    path('booking/<int:pid>/', views.booking, name="BookPackage"),
    path('mybooking/', views.mybooking, name="Mybookings"),
    path('mypackage/<int:bid>/', views.mypackage, name="MyPackage"),
    path('cancelbooking/<int:cid>', views.cancelbooking, name="Cancelbookings"),
    path('feedBack/', views.feedBack, name="feedBack")
    
]
