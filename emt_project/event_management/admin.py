from django.contrib import admin
from django.contrib import admin
from .models import (
	Emt_c,
	Category,
	Services,
	Package,
	)
# Register your models here.
class Emt_cAdmin(admin.ModelAdmin):
	list_display = ["id","comp_name","user"]
	class Meta:
		model = Emt_c

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["id","category_name"]
	class Meta:
		model = Category

class ServicesAdmin(admin.ModelAdmin):
	list_display = ["id","service_name"]
	class Meta:
		model = Services

class PackageAdmin(admin.ModelAdmin):
	list_display = ["id","package_type","package_cost","package_emt"]
	class Meta:
		model = Package

admin.site.register(Emt_c,Emt_cAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Package,PackageAdmin)