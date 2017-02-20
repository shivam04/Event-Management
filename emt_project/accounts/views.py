from django.shortcuts import render, redirect
from .models import NormalUser,CorporateUser
from django.contrib.auth.models import User
from django.http import HttpResponse , HttpResponseRedirect , Http404,HttpResponseForbidden, HttpResponseBadRequest
from rest_framework.test import RequestsClient,APIRequestFactory
from django.middleware import csrf
from django.http import JsonResponse
import json
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
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
		#print username,password
		url = "http://"+host+"/api/users/alluser/create/"
		#print url
		response = client.post(url, json={
				    'username': username,
				    'first_name':firstname,
				    'last_name':lastname,
				    'email':email,
				    'password':password,
				}, headers={'X-CSRFToken': csrftoken})
		# print response.status_code
		# print response.json()
		if response.status_code==201:
			user = response.json()
			user_id = user['id']
			#print user_id
			nurl = "http://"+host+"/api/users/normalusers/create/"
			
			response_n = client.post(nurl, json={
				    'user': user_id,
				    'aadhar_card':aadhar,
				}, headers={'X-CSRFToken': csrftoken})
			# print response_n.status_code
			if response_n.status_code == 201:
				return redirect("/")
		elif response.status_code == 400:
			data = response.json()
			request.session['Error'] = data
			# data = response.json()
			# data= json.loads(json.dumps(data))
			# print data['username'][0]
			# if 'username' in data:
			# 	request.session['Error']['username'] = data['username'][0]
			# 	#print data['username']
			# if 'password' in data:
			# 	request.session['Error']['password'] = data['password'][0]
			# 	#print data['password']
			# if 'email' in email:
			# 	request.session['Error']['email'] = data['email'][0]	
			return redirect("/")
	
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

def login_view(request):
	client = RequestsClient()
	if request.method=="POST":
		csrftoken = request.POST.get("csrfmiddlewaretoken")
		username = request.POST.get("username")
		password = request.POST.get("password")
		# host = request.META['HTTP_HOST']
		# url = "http://"+host+"/api/auth/token/"
		# data = client.post(url,json={
		# 		'username':username,
		# 		'password':password, 
		# 	},headers={'X-CSRFToken':csrftoken}).json()
		# request.session['token'] = data['token']
		# print request.session['token']
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			if request.user.is_authenticated():
				return redirect('/')
			else:
				return HttpResponseForbidden()
		else:
			return HttpResponseForbidden()
	else:
		return HttpResponseForbidden()
def logout_view(request):
	logout(request)
	return redirect("/")