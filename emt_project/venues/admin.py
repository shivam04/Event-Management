from django.contrib import admin
from .models import (
	City,
	Venues,
	Locality,
	Address,
	)
class CityAdmin(admin.ModelAdmin):
	list_display = ["id","city_name"]
	class Meta:
		model = City

class LocalityAdmin(admin.ModelAdmin):
	list_display = ["id","locality_name"]
	class Meta:
		model = City

class VenuesAdmin(admin.ModelAdmin):
	list_display = ["id","venue_name","venue_locality","venue_city"]
	class Meta:
		model = City

class AddressAdmin(admin.ModelAdmin):
	list_display = ["id","venue","address_line","zip_code"]
	class Meta:
		model = City


admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Venues,VenuesAdmin)
admin.site.register(Address,AddressAdmin)