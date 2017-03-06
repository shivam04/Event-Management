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
	print k
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
			#print description
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
				#print nurl
				res = client.get(nurl);
				#print res
				p =  res.json()
				venue_name = p['venue_name']
				content_type = p['content_type']
				object_id = p['object_id']
				#print p
				r = client.put(nurl,data={
					'venue_name':venue_name,
					'content_type':content_type,
					'venue_city':city_name,
					'venue_locality':locality_name,
					'object_id':object_id,
					})
				#print r.json()
				ven_js = r.json()
				if r.status_code==200:
					ven_id = int(ven_js['object_id'])
					h= ven_id
					#print h
					ven_id = Venues.objects.filter(id=ven_js['id']).first()
					address = Address(venue=ven_id,address_line=address,zip_code=pin,lon='0.0',let='0.0')
					address.save()
					return redirect('/corporate/clubcreate/2?q='+str(h))
		elif k=="2":
			n= request.GET.get('q')
			single = request.POST.get('single')
			single_price = 0
			couple_price = 0
			couple = request.POST.get('couple')
			s1 = request.POST.get("s1")
			s2 = request.POST.get("s2")
			s3 = request.POST.get("s3")
			s4 = request.POST.get("s4")
			s5 = request.POST.get("s5")
			print s1,s2,s3,s4,s5
			club = Club.objects.filter(id=n).first()
			#return redirect('/corporate/clubcreate/2?q='+str(39))
			if single != None:
				single_price = request.POST.get('single_fee')
				
				#print club.club_name
				entry_type = Entry_Type.objects.filter(id=1).first()

				entry_type_s = Entry_rate(club_name=club,entry_type_r=entry_type,price=single_price)
				entry_type_s.save()
			if couple!=None:
				couple_price = request.POST.get('couple_fee')
				#single_price = request.POST.get('single_fee')
				#entry_type_s = Entry_rate(club_name=n,entry_type_r=1,price=single_price)
				#club = Club.objects.filter(id=n).first()
				entry_type = Entry_Type.objects.filter(id=4).first()
				entry_type_c = Entry_rate(club_name=club,entry_type_r=entry_type,price=couple_price)
				entry_type_c.save()
			#s1 = re
			if s1!=None:
				service1 = Service(service_name=s1,club_name=club)
				service1.save()
			if s2!=None:
				service2 = Service(service_name=s2,club_name=club)
				service2.save()
			if s3!=None:
				service3 = Service(service_name=s3,club_name=club)
				service3.save()
			if s4!=None:
				service4 = Service(service_name=s4,club_name=club)
				service4.save()
			if s5!=None:
				service5 = Service(service_name=s5,club_name=club)
				service5.save()	
			print n
			return redirect("/corporate/")


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
			print request.GET.get('q')
			return render(request,'register3c.html',{})