from django.contrib import admin
from .models import (
	Club,
	Entry_rate,
	Service,
	)
class ClubAdmin(admin.ModelAdmin):
	list_display = ["id","club_name"]
	class Meta:
		model = Club

class Entry_rateAdmin(admin.ModelAdmin):
	list_display = ["id","entry_type","club_name","price"]
	class Meta:
		model = Club

class ServiceAdmin(admin.ModelAdmin):
	list_display = ["id","service_name","club_name",]
	class Meta:
		model = Club



admin.site.register(Club,ClubAdmin)
admin.site.register(Entry_rate,Entry_rateAdmin)
admin.site.register(Service,ServiceAdmin)
