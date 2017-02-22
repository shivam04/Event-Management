from django.shortcuts import render

# Create your views here.
def book(request,slug):
	venue = request.session.pop('venue')
	print venue
	return render(request,"book.html",{'title':'Book'})