from django.conf.urls import url
from django.contrib import admin
from .views import (
    register,
    test,
    login_view,
    logout_view,
    corporate_register,
    )
urlpatterns = [
    url(r'^register$', register, name='register'),
    url(r'^corporate-register$', corporate_register, name='corporate-register'),
    url(r'^login/$',login_view, name='login'),
    url(r'^logout$',logout_view, name='logout'),
    url(r'^test/$',test,name="test"),
]