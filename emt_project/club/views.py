from django.shortcuts import render
from django.conf import settings
from rest_framework.test import RequestsClient,APIRequestFactory
import requests
import json
from venues.models import City,Locality
# Create your views here.
def register_club(request):
	host =  request.META['HTTP_HOST'] 
	url =  'http://'+host+'/api/clubs/create/'
	client = RequestsClient()
	#print request.user
	if request.method=="POST":
		
		club_name = request.POST.get("club_name")
		csrftoken = request.POST.get("csrfmiddlewaretoken")
		city_name = request.POST.get("city");
		locality_name = request.POST.get("locality");
		#print city_name,locality_name
		#client = RequestsClient()

		response = client.post(url, json={
				    'club_name': club_name,
				    'user':request.user.id,
				}, headers={'X-CSRFToken': csrftoken})
		print response.status_code
		js =  response.json()
		#print response.status_code
		u = js['venue']['update']
		if response.status_code == 201:
			clit = APIRequestFactory()
			nurl = 'http://'+host+u;
			print nurl
			res = client.get(nurl);
			print res
			p =  res.json()
			venue_name = p['venue_name']
			content_type = p['content_type']
			object_id = p['object_id']
			r = client.put(nurl,data={
				'venue_name':venue_name,
				'content_type':content_type,
				'venue_city':city_name,
				'venue_locality':locality_name,
				'object_id':object_id,
				})
			print r
		#token = request.POST.get('csrfmiddlewaretoken')
		#a = factory.post('http://127.0.0.1:8000/api/clubs/create/',{'club_name':club_name},format=json)
		#print response.json()
	cities = City.objects.all();
	locality = client.get("http://127.0.0.1/api/venues/citylocality")
	locality = json.dumps(locality.json())
	#print locality
	context={
	'cities':cities,
	'locality':locality,
	}
	return render(request, "index.html",context)