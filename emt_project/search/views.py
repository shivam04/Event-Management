from django.shortcuts import render
from venues.models import City,Locality
from rest_framework.test import RequestsClient,APIRequestFactory
from django.http import HttpResponse , HttpResponseRedirect , Http404
import json
# Create your views here.
def index(request):
	if request.session.has_key('Error'):
		error = request.session.pop('Error', False)
		#print error['username'][0]
		error = json.dumps(error)
		print error
	else:
		error =None

	client = RequestsClient()
	cities = City.objects.all();
	# verify_token = client.post("http://127.0.0.1/api/verify/token/",json={
	# 	'token':request.session['token']
	# 	})
	# print request.session['token']
	# if verify_token.status_code==400:
	# 	refresh_token = client.post("http://127.0.0.1/api/refresh/token/",json={
	# 	'token':request.session['token']
	# 	}).json()
	# 	print refresh_token
		# request.session['token'] = refresh_token['token']	
	
	# locality = client.get("http://127.0.0.1/api/venues/citylocality",headers={
	# 	'Authorization':'JWT '+request.session['token'],
	# 	})
	locality = client.get("http://127.0.0.1/api/venues/citylocality")
	#print locality.json()
	locality = json.dumps(locality.json())
	user =""
	if request.user:
		user = request.user
		print user.username
	else:
		user = None
	context={
	'cities':cities,
	'locality':locality,
	'error':error,
	'user':user,
	'next':'',
	}
	#print locality
	return render(request, "index.html",context)

def retrieve(request):
	client = RequestsClient()
	if request.method == 'POST':
		print request.method
		city = request.POST['city']
		locality = request.POST['locality']
		venue = request.POST['venue']
		#print venue
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
			request.session['venue'] = 'club'
			url = 'http://127.0.0.1/api/clubs/?city='+city+'&locality='+locality
			#print request.session['token']
			# venues = client.get(url,headers={
			# 	'Authorization':'JWT '+request.session['token'],
			# 	})
			venues = client.get(url)
			venues = venues.json()
			print venues
			context = {
			'ven':'club',
			'venues':venues,
			'title':'Search',
			'next':'',
			}
			return render(request, "reservation-step-2.html",context)
	else:
		raise Http404

def search_service(request,service):
	if service=="club":
		request.session['venue'] = 'club'
		client = RequestsClient()
		url = 'http://127.0.0.1/api/clubs/'
		venues = client.get(url)
		venues = venues.json()
		print venues
		return render(request,"reservation-step-2.html",{'venues':venues,'title':'Club','ven':'club','next':'/club/search/'})
	elif service=="venue":
		return render(request,"reservation-step-2.html",{})
	elif service=="marriage":
		return render(request,"reservation-step-2.html",{})
	else:
		return render(request,"reservation-step-2.html",{})

def about(request):
	return render(request,'about.html',{'title':'About'})

def contact(request):
	return render(request,'contact.html',{'title':'Contact'})