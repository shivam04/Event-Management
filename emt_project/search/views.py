from django.shortcuts import render
from venues.models import City,Locality
from rest_framework.test import RequestsClient,APIRequestFactory
from django.http import HttpResponse , HttpResponseRedirect , Http404
import json
# Create your views here.
def index(request):
	client = RequestsClient()
	cities = City.objects.all();
	locality = client.get("http://127.0.0.1/api/venues/citylocality")
	locality = json.dumps(locality.json())
	#print locality
	context={
	'cities':cities,
	'locality':locality,
	}
	print locality
	return render(request, "index.html",context)

def retrieve(request):
	client = RequestsClient()
	if request.method == 'POST':
		city = request.POST['city']
		locality = request.POST['locality']
		venue = request.POST['venue']
		print venue
		# city_detail = client.get("http://127.0.0.1/api/venues/"+city)
		# city_detail = city_detail.json()
		# locality_detail = client.get("http://127.0.0.1/api/venues/locality/"+locality)
		# localities =  locality_detail.json()
		# if localities['city'] == city_detail['city_name']:
		# 	venues = localities['venue']
		# 	print venues
		# 	context = {
		# 	'venues':venues,
		# 	}
		if venue=='club':
			url = 'http://127.0.0.1/api/clubs/?city='+city+'&locality='+locality
			print url
			venues = client.get(url)
			venues = venues.json()
			context = {
			'venues':venues,
			}
			return render(request, "reservation-step-2.html",context)
	else:
		raise Http404