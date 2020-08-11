from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
	list_display = ('id','title','is_published','price','list_date', 'salesman')
	list_display_links =('id','title')
	list_filter= ('salesman',)
	list_editable=('is_published',)
	search_fields=('title','description','address','city','state','zipcode','price','make')
	list_per_page= 25
admin.site.register(Car,CarAdmin)



