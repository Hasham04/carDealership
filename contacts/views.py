from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.
def contact(request):
	if request.method == 'POST':
		car_id = request.POST['car_id']
		print(car_id)
		car = request.POST['car']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		salesman_email = request.POST['salesman_email']

		# check if user is authenticated
		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(car_id = car_id, user_id=user_id)
			if has_contacted:
				messages.error(request,'You have already made an inquiry for this listing')
				print("WE ARE HERE")
				return redirect('/cars/'+ car_id)

		contact = Contact(car=car, car_id=car_id,name=name,email=email,
			phone=phone,message=message,user_id=user_id)
		contact.save()

		send_mail(
			subject='Car Listing Inquiry',
			message='There has been an inquiry for ' + car + '. Sign into the admin panel for more info',
			from_email='hasham610@gmail.com',
			recipient_list=[salesman_email]
			)
		messages.success(request,'Your request has been submitted, a salesperson will get back to you soon')
		return redirect('/cars/'+ car_id)
