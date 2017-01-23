from django.conf.urls import url
from django.contrib import admin
from .views import (
    CityListAPIView,
    CityDetailAPIView,
    LocalityListAPIView,
    LocalityDetailAPIView,
    VenueCreateAPIView,
    VenueUpdateAPIView,
    CityLocalityListAPIView,
    )
urlpatterns = [
    url(r'^$', CityListAPIView.as_view(), name='list'),
    url(r'^citylocality/$',CityLocalityListAPIView.as_view(),name="citylist"),
    url(r'^create/$', VenueCreateAPIView.as_view(), name='create'),

    url(r'locality/$',LocalityListAPIView.as_view(),name='locality_list'),

    url(r'locality/(?P<locality_slug>[\w-]+)/$',LocalityDetailAPIView.as_view(),name='locality_detail'),

    url(r'^(?P<city_slug>[\w-]+)/$',CityDetailAPIView.as_view(),name='detail'),
    url(r'^single-venue/(?P<id>\d+)/edit/$', VenueUpdateAPIView.as_view(),name="update"),
    
    #url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<pk>\d+)/edit$', CommentDetailAPIView.as_view(), name='edit'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]