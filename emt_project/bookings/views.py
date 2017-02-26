from django.shortcuts import render
from rest_framework.test import RequestsClient,APIRequestFactory
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse , HttpResponseRedirect , Http404,HttpResponseForbidden, HttpResponseBadRequest
import json
from club.models import *
from .models import *
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import datetime
from django.utils.crypto import get_random_string
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from cgi import escape
def index(request):
	#print request.GET.get('firstname')
	data = {
        'firstname': request.GET.get('firstname'),
        'lastname': request.GET.get('lastname'),
        'email':request.GET.get('email'),
        'contact':request.GET.get('contact'),
        'venue':request.GET.get('venue'),
        'price':request.GET.get('price'),
        'paymentmethod':request.GET.get('paymentmethod'),
        'fromdate' :request.GET.get('fromdate'),
        'todate' :request.GET.get('todate'),
        'id':request.GET.get('id')
    }
	data['fromdate'] = datetime.datetime.strptime(data['fromdate']+" 20:00:00", '%m/%d/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
	data['todate'] = datetime.datetime.strptime(data['todate']+" 00:00:00", '%m/%d/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
	status = Status.objects.filter(id=1).first()
	book = Booking(fromdate=data['fromdate'],todate=data['todate'],total=data['price'],
		user=request.user,status_id=status)
	book.save()
	last_invoice = Payment.objects.all().order_by('id').last()
	invoice_no = last_invoice.invoice_number
	invoice_int = int(invoice_no)
	invoice_int+=1
	invoice_number = str(invoice_int)
	invoice_number = '0'*(8-len(invoice_number))+invoice_number
	paymentmethod = Payment_Method.objects.filter(id=data['paymentmethod']).first()
	tansaction_number = get_random_string(length=10)
	payment = Payment(invoice_number=invoice_number,payment_method=paymentmethod,booking_id=book,
		tansaction_number=tansaction_number,amount=data['price'],user=request.user)
	payment.save()
	content_type = ContentType.objects.filter(model=data['venue']).first()
	print content_type.id
	object_id = data['id']
	order_venue = OrderVenue(venue_type=content_type,object_id=object_id,booking_id=book)
	order_venue.save()
	print book.id
	print payment.id
	print order_venue.id
	response = create_pdf(data,request)
	#print response
	return response
def create_pdf(data,request):
	template = get_template("ss.html")
	#print template.render() 
	#context = Context(context_dict)
	html  = template.render()
	result = StringIO.StringIO()
	print result.getvalue()
	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
	#print pdf.err
	if not pdf.err:
	    response = HttpResponse(result.getvalue(), content_type='application/pdf')
	    response['Content-Disposition'] = 'attachment; filename="k.pdf"'
	    return response
	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
def book(request,slug):
	date = request.GET.get('date')
	entry = request.GET.get('entry')
	group = request.GET.get('guests')
	print date,entry,group
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
	entry_type = Entry_Type.objects.filter(id=entry).first()
	price = Entry_rate.objects.filter(club_name=club_name,entry_type_r=entry).first()
	price= price.price
	entry = entry_type.type_entry
	guests = False
	if entry == "Group":
		if group=="":
			group=1
		price = price*int(group)
		guests = int(group)
	ven_ids = Club.objects.filter(club_slug=slug).first().id
	book_data = json.loads(json.dumps({'date':date,'entry':entry,'price':price,'guests':guests,'slug':slug}))
	
	return render(request,"book.html",{'ven_ids':ven_ids,'venue':venue,'title':'Book','next':'/book/'+slug+'/','data':data,'book_data':book_data})