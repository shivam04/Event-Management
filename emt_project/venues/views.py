from django.shortcuts import render
# import requests
# from rest_framework.views import APIView
# from .models import City
# from .serializers import CityListSerializer
# import json
# from rest_framework.response import Response
# class CityListApiView(APIView):
# 	def get(self,request):
# 		queryset = City.objects.all()
# 		serializer = CityListSerializer(queryset,many=True)
# 		# a =  json.dumps(serializer.data[0])
# 		# a = json.loads(a)
# 		# #print a
# 		# context = {
# 		# 'id':a['id'],
# 		# 'city_name':a['city_name'],
# 		# 'total_locality':a['total_locality'],
# 		# 'total_venues':a['total_venues'],
# 		# }
# 		#print context
# 		return Response(serializer.data)

# def list_view(request):
# 	a = requests.get('http://127.0.0.1:8000/api/venue/')
# 	a =  a.json()
# 	a =  a[0]
# 	context = {
# 		'id':a['id'],
# 		'city_name':a['city_name'],
# 		'total_locality':a['total_locality'],
# 		'total_venues':a['total_venues'],
# 		}
# 	return render(request,'index.html',context)

