from django.shortcuts import render ,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, make_choices, bodyType_choices
# Create your views here.
from .models import Car


def index(request):
	cars=Car.objects.order_by('-list_date').filter(is_published=True)
	paginator= Paginator(cars,3)
	page= request.GET.get('page')
	page_listings=paginator.get_page(page)


	context={'cars':page_listings}
	return render(request,'cars/cars.html',context)

def car(request,car_id):
	car=get_object_or_404(Car,pk=car_id)

	context={'car':car}
	return render(request,'cars/car.html',context)
	
def search(request):
	queryset_list = Car.objects.order_by('-list_date')
	#keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)
	#keywords
	if 'address' in request.GET:
		address = request.GET['address']
		if address:
			queryset_list = queryset_list.filter(address__icontains=address)

	if 'make' in request.GET:
		make = request.GET['make']
		if make:
			queryset_list = queryset_list.filter(make__iexact=make) #lte means less than or equal to

	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte=price) 

	if 'bodyType' in request.GET:
		bodyType = request.GET['bodyType']
		if bodyType:
			queryset_list = queryset_list.filter(bodyType__iexact=bodyType)


	context={

		'price_choices': price_choices,
		'make_choices': make_choices,
		'bodyType_choices': bodyType_choices,
		'cars': queryset_list,
		'values': request.GET
	}
	return render(request,'cars/search.html',context)
