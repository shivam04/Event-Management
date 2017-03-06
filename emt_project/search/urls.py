from django.conf.urls import url
from django.contrib import admin
from .views import (
	index,
    retrieve,
    search_service,
    about,
    contact,
    test,
	)
urlpatterns = [
    #url(r'^$', ClubListAPIView.as_view(), name='list'),
    # url(r'locality/$',LocalityListAPIView.as_view(),name='locality_list'),
    # url(r'locality/(?P<locality_slug>[\w-]+)/$',LocalityDetailAPIView.as_view(),name='locality_detail'),
    # url(r'^(?P<city_slug>[\w-]+)/$',CityDetailAPIView.as_view(),name='detail')

    url(r'^$', index, name='index'),
    url(r'^(?P<service>[\w-]+)/search/$',search_service,name="search_service"),
    url(r'search/$',retrieve,name='search_venue'),
    url(r'about/$',about,name='about'),
    url(r'contact/$',contact,name='contact'),
    url(r'test/$',test,name='test'),
    #url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<pk>\d+)/edit$', CommentDetailAPIView.as_view(), name='edit'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]