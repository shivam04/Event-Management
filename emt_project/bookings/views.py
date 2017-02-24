from django.shortcuts import render
from rest_framework.test import RequestsClient,APIRequestFactory
from django.http import JsonResponse
from django.http import HttpResponse , HttpResponseRedirect , Http404,HttpResponseForbidden, HttpResponseBadRequest
import json
from club.models import *
# Create your views here.
def index(request):
	#print request.GET.get('firstname')
	data = {
        'firstname': request.GET.get('firstname'),
        'lastname': request.GET.get('lastname'),
        'email':request.GET.get('email'),
        'contact':request.GET.get('contact'),
    }
	print data
	return JsonResponse(data)
def book(request,slug):
	date = request.GET.get('date')
	entry = request.GET.get('entry')
	#print date,entry
	client = RequestsClient()
	host =  request.META['HTTP_HOST']
	data = None
	if request.user.is_authenticated():
		#print request.user.id
		url = 'http://'+host+'/api/users/normalusers?user='+str(request.user.id)
		#print url
		nurl = client.get(url).json()[0]['url']
		#print nurl
		data = client.get(nurl).json()
		data['user_detail'] = data['user_detail'][0]
		#print data
		# user = data
	else:
		data = False
	venue = request.session['venue']
	entry = entry.title()
	club_url = 'http://'+host+'/api/clubs/'+slug+'/'
	club_detail = client.get(club_url)
	#print club_detail.status_code
	if club_detail.status_code==200:
		club_detail = club_detail.json()
	else:
		return HttpResponseBadRequest()
	#print club_detail
	club_name = club_detail['id']
	price = Entry_rate.objects.filter(club_name=club_name,entry_type=entry).first()
	price= price.price
	book_data = json.loads(json.dumps({'date':date,'entry':entry,'price':price}))
	
	return render(request,"book.html",{'title':'Book','next':'/book/'+slug+'/','data':data,'book_data':book_data})