from django.shortcuts import render
from rest_framework.test import RequestsClient,APIRequestFactory
# Create your views here.
def book(request,slug):
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
	venue = request.session.pop('venue')
	print venue
	return render(request,"book.html",{'title':'Book','next':'/book/'+slug+'/','data':data})