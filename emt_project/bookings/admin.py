from django.contrib import admin
from .models import(
	Status,
	Booking,
	Payment_Method,
	Payment,
	OrderVenue,
	)
class StatusAdmin(admin.ModelAdmin):
	list_display = ['id','status_name']
	class Meta:
		model = Status
class BookingAdmin(admin.ModelAdmin):
	list_display = ['id','fromdate','status_id','todate','total','date_time','user']
	class Meta:
		model = Booking
class Payment_MethodAdmin(admin.ModelAdmin):
	list_display = ['id','payment_method']
	class Meta:
		model = Payment_Method
class PaymentAdmin(admin.ModelAdmin):
	list_display = ['id','invoice_number','payment_method','booking_id','tansaction_number','amount','date_time','user']
	class meta:
		model = Payment
class OrderVenueAdmin(admin.ModelAdmin):
	list_display = ['id','venue_type','object_id','venue_object','booking_id']
	class Meta:
		model = OrderVenue
admin.site.register(Status,StatusAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Payment_Method,Payment_MethodAdmin)
admin.site.register(OrderVenue,OrderVenueAdmin)
admin.site.register(Payment,PaymentAdmin)
# Register your models here.
