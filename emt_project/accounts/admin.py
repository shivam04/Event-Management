from django.contrib import admin
from .models import (
	NormalUser,
	CorporateUser,
	)
# Register your models here.
class NormalUserAdmin(admin.ModelAdmin):
	list_display = ["id","user","aadhar_card"]
	class Meta:
		model = NormalUser

class CorporateUserAdmin(admin.ModelAdmin):
	list_display = ["id","user","aadhar_card","comapny_name"]
	class Meta:
		model = CorporateUser
admin.site.register(NormalUser,NormalUserAdmin)
admin.site.register(CorporateUser,CorporateUserAdmin)