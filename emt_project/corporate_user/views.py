from django.shortcuts import render,redirect
from .models import *
from club.models import *
from venues.models import *
from rest_framework.test import RequestsClient,APIRequestFactory
import json
def index(request):
	return render(request,'index-3.html',{})

def club_create(request,pk=1):
	k =  str(pk)
	client = RequestsClient()
	if request.method=="POST":
		if k=="1":
			host =  request.META['HTTP_HOST'] 
			url =  'http://'+host+'/api/clubs/create/'
			club_name = request.POST.get('club-name')
			address = request.POST.get('Add1')
			city_name = request.POST.get("city");
			locality_name = request.POST.get("locality")
			pin = request.POST.get("pin")
			license = request.POST.get("license")
			description = request.POST.get("description")
			csrftoken = request.POST.get("csrfmiddlewaretoken")
			print description
			response = client.post(url, json={
				    'club_name': club_name,
				    'user':request.user.id,
				    'description':description,
				}, headers={'X-CSRFToken': csrftoken})
			js =  response.json()
		#print response.status_code
		u = js['venue']['update']
		if response.status_code==201:
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
			ven_js = r.json()
			if r.status_code==200:
				ven_id = int(ven_js['id'])
				ven_id = Venues.objects.filter(id=ven_js['id']).first()
				address = Address(venue=ven_id,address_line=address,zip_code=pin,lon='0.0',let='0.0')
				address.save()
				return redirect('/corporate/clubcreate/2')
	else:
		if k=="1":
			print "hell"
			cities = City.objects.all();
			locality = client.get("http://127.0.0.1/api/venues/citylocality")
			locality = json.dumps(locality.json())
			#print locality
			context={
			'cities':cities,
			'locality':locality,
			}
			return render(request,'reg2c.html',context)
		elif k=="2":
			return render(request,'register3c.html',{})