from django.contrib import admin
 
from .models import Salesman

class SalesmanAdmin(admin.ModelAdmin):
	list_display=('id','name','email','hire_date')
	list_display_links=('id','name')
	list_per_page=25


admin.site.register(Salesman,SalesmanAdmin)