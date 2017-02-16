from django.conf.urls import url
from django.contrib import admin
from .views import (
    register,
    test,
    )
urlpatterns = [
    url(r'^register$', register, name='register'),
    url(r'^test/$',test,name="test"),
]