from django.shortcuts import render
from cars.models import Car
from salesman.models import Salesman
from cars.choices import price_choices, make_choices, state_choices, bodyType_choices

def index(request):
	cars= Car.objects.order_by('-list_date').filter(is_published=True)[:3]
	context={'cars':cars,'price_choices':price_choices,'make_choices':make_choices,'state_choices':state_choices,'bodyType_choices':bodyType_choices}
	return render(request,'pages/index.html',context)

def about(request):
	#get all realtors
	salesman = Salesman.objects.order_by('-hire_date')
	# Get MVP
	mvp_salesman=Salesman.objects.all().filter(is_mvp=True)

	context={
		'salesman':salesman,
		'mvp_salesman': mvp_salesman
	}

	return render(request,'pages/about.html',context)