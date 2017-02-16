from django.shortcuts import render, redirect
from .models import NormalUser,CorporateUser
from django.contrib.auth.models import User
from django.http import HttpResponse , HttpResponseRedirect , Http404,HttpResponseForbidden, HttpResponseBadRequest
from rest_framework.test import RequestsClient,APIRequestFactory
from django.middleware import csrf
def register(request):
	client = RequestsClient()
	if request.method=="POST":
		host =  request.META['HTTP_HOST']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		contact = request.POST['contact']
		email = request.POST['email']
		password = request.POST['password']
		username = request.POST['username']
		csrftoken = request.POST.get("csrfmiddlewaretoken") 
		aadhar = request.POST['aadhar']
		url = "http://"+host+"/api/users/alluser/create/"
		#print url
		response = client.post(url, json={
				    'username': username,
				    'first_name':firstname,
				    'last_name':lastname,
				    'email':email,
				    'password':password,
				}, headers={'X-CSRFToken': csrftoken})
		#print response.status_code
		if response.status_code==201:
			user = response.json()
			user_id = user['id']
			#print user_id
			nurl = "http://"+host+"/api/users/normalusers/create/"
			
			response_n = client.post(nurl, json={
				    'user': user_id,
				    'aadhar_card':aadhar,
				}, headers={'X-CSRFToken': csrftoken})
			#print response_n.status_code
			if response_n.status_code == 201:
				k = response_n.json()
				#print k['aadhar_card']
				return redirect("/")
		elif response.status_code == 400:
			request.session['Error'] = 'Username Or Password Missing'
			return  redirect("/")
	
	else:
		return HttpResponseForbidden()

def test(request):
	client = RequestsClient()
	if request.method=="POST":
		csrftoken = request.POST.get("csrfmiddlewaretoken")
		host =  request.META['HTTP_HOST']
		nurl = "http://"+host+"/api/users/normalusers/create/"
		response_n = client.post(nurl, json={
					    'user': 10,
					    'aadhar_card':"45466465484",
					}, headers={'X-CSRFToken': csrftoken})
		print response_n.status_code
		return redirect("/")
	else:
		return render(request,"ff.html",{})
