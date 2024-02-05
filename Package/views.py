from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Packages, Package_details, Booking, Contact, FeedBack

# Create your views here.


def index(request):
	p = Packages.objects.all()
	list1 = []
	for i in range(3):
		list1.append(p[i])
	return render(request, 'index.html', {
		'package' : list1,
		})


def about(request):
	return render(request, 'about.html')


def whyus(request):
	return render(request, 'service.html')


def testimonial(request):
	f = FeedBack.objects.all()
	return render(request, 'testimonial.html', {
		'feedBack' : f
		})


def contact(request):
	if request.method == "POST":
		cname = request.POST['Name']
		cemail = request.POST['Email']
		cphone = request.POST['Phone']
		cmsg = request.POST['Message']

		con = Contact(c_name=cname, c_email=cemail, c_phone=cphone, c_msg=cmsg)
		con.save()
		return render(request, 'contact.html', {
			'yes' : "yes",
			'msg' : "Thank you for contacting us..."
			})
	else:
		return render(request, 'contact.html', {
			'yes' : "no"
			})


def handlesignup(request):
	u = User.objects.all()
	l1 = []
	for i in u:
		l1.append(i.username)

	if request.method == 'POST':
		# get parameters
		username = request.POST['email']
		email = request.POST['email']
		fname = request.POST['firstname']
		lname = request.POST['lastname']
		pass1 = request.POST['passwd']
		if username in l1:
			return render(request, 'register.html',{
				'yes' : "yes",
				'msg' : "Email already exists.."
			})

		# Create user
		myuser = User.objects.create_user(username, email, pass1)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser.save()
		return render(request,'register.html', {
			'yes' : "yes",
			'msg' : "Successfully signed up..."
		})


def handlesignin(request):
	p = Packages.objects.all()
	if request.method == 'POST':
		loginusername = request.POST['username']
		loginpassword = request.POST['password']

		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			login(request,user)
			return render(request, 'home.html', {
				'package' : p,
				'yes' : "yes",
				'msg' : "Successfully logged in.."
			})
		else:
			return render(request,'register.html', {
				'yes' : "yes",
				'msg' : "Invalid User..."
			})
	return render(request, 'register.html')


def handlelogout(request):
	logout(request)
	p = Packages.objects.all()
	list1 = []
	for i in range(3):
		list1.append(p[i])
	return render(request, 'index.html', {
		'package' : list1,
		'yes' : "yes",
		'msg' : "Successfully Logged Out"
		})


def home(request):
	p = Packages.objects.all()
	return render(request, 'home.html', {
			'package' : p,
			})


def packages(request):
	p = Packages.objects.all()
	return render(request, 'packages.html', {
		'package' : p,
		'yes' : "no",
		})


def subpackage(request, mypackage):
	subp = Package_details.objects.all()
	list1 = []
	for i in subp:
		if i.p_package.package == mypackage:
			list1.append(i)

	return render(request, 'subpackage.html', {
		'subpackage' : list1,
		'pac' : mypackage,
		})


def checkout(request, myid):
	pac1 = Package_details.objects.filter(p_id=myid)
	return render(request, 'checkout.html', {
		'p' : pac1[0],
		})


def booking(request, pid):
	booking_of = Package_details.objects.filter(p_id=pid)
	p = Packages.objects.all()
	if request.method == "POST":
		baddress = request.POST.get('uadd', '')
		bcontact = request.POST.get('ucontact', '')
		boarding = request.POST.get('uboarding', '')
		bdate = request.POST.get('udate', '')
		btravellers = request.POST.get('utraveller', '')
		broom = request.POST.get('uroom', '')

		book = Booking(booking_user=request.user, booking_package=booking_of[0], booking_address=baddress,
			booking_phone=bcontact, boarding=boarding, start_date=bdate, travellers=btravellers, room_wise=broom)
		book.save()
		return render(request, 'home.html', {
			'package' : p,
			'yes' : "yes",
			'msg' : f"Thanks For Booking, You will get a call soon from the {booking_of[0].p_provider_name}."
			})


def mybooking(request):
	u1 = Booking.objects.filter(booking_user=request.user)
	return render(request, 'mybooking.html', {
		'booking' : u1,
		'book' : len(u1),
		})


def mypackage(request, bid):
	u2 = Booking.objects.filter(booking_id=bid)
	return render(request, 'mypackage.html', {
		'b' : u2[0],
		})


def cancelbooking(request, cid):
	p = Packages.objects.all()
	c = Booking.objects.filter(booking_id=cid)
	c.delete()
	return render(request, 'home.html', {
		'package' : p,
		'yes' : "yes",
		'msg' : "Your booking is cancelled.."
		})


def feedBack(request):
	u1 = Booking.objects.filter(booking_user=request.user)
	if request.method == "POST":
		msg = request.POST.get('umsg', '')
		f = FeedBack(f_user=request.user, f_msg=msg)
		f.save()
		return render(request, 'mybooking.html', {
			'booking' : u1,
			'book' : len(u1),
			'yes' : "yes",
			'msg' : "Thank You For Your feedBack."
			})