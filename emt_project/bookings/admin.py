from django.contrib import admin
from .models import(
	Status,
	Booking,
	Payment_Method,
	Payment,
	OrderVenue,
	)
admin.site.register(Status)
admin.site.register(Booking)
admin.site.register(Payment_Method)
admin.site.register(OrderVenue)
admin.site.register(Payment)
# Register your models here.
