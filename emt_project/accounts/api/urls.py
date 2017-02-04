from django.conf.urls import url
from django.contrib import admin
from .views import (
    NormalListAPIView,
    NormalDetailAPIView,
    NormalUserCreateAPIView,
    )
urlpatterns = [
    url(r'^normalusers$', NormalListAPIView.as_view(), name='list'),
    # url(r'locality/$',LocalityListAPIView.as_view(),name='locality_list'),
    # url(r'locality/(?P<locality_slug>[\w-]+)/$',LocalityDetailAPIView.as_view(),name='locality_detail'),
    url(r'^normalusers/(?P<id>\d+)/$',NormalDetailAPIView.as_view(),name='user_detail'),
    url(r'^normalusers/create/$', NormalUserCreateAPIView.as_view(), name='user_create'),
    #url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<pk>\d+)/edit$', CommentDetailAPIView.as_view(), name='edit'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]