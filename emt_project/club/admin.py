from django.contrib import admin
from .models import (
	Club,
	Entry_rate,
	Service,
	Entry_Type,
	)
class ClubAdmin(admin.ModelAdmin):
	list_display = ["id","club_name","user"]
	class Meta:
		model = Club

class Entry_rateAdmin(admin.ModelAdmin):
	list_display = ["id","entry_type_r","club_name","price"]
	class Meta:
		model = Entry_rate

class ServiceAdmin(admin.ModelAdmin):
	list_display = ["id","service_name","club_name",]
	class Meta:
		model = Service

class Entry_TypeAdmin(admin.ModelAdmin):
	list_display = ["id","type_entry"]
	class Meta:
		model = Entry_Type

admin.site.register(Club,ClubAdmin)
admin.site.register(Entry_rate,Entry_rateAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Entry_Type,Entry_TypeAdmin)
