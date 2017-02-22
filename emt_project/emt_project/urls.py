"""emt_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include,url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token,refresh_jwt_token
from django.conf.urls.static import static
#from search.views import index
#from venues.views import list_view,CityListApiView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/verify/token/', verify_jwt_token),
    url(r'^api/refresh/token/', refresh_jwt_token),
    #url(r'^venue/',list_view),
    url(r'^accounts/',include("accounts.urls",namespace="accounts")),
    url(r'^api/venues/',include("venues.api.urls",namespace='venue-api')),
    url(r'^api/clubs/',include("club.api.urls",namespace='club-api')),
    url(r'^api/users/',include("accounts.api.urls",namespace="users-api")),
    url(r'^clubs/',include("club.urls",namespace="club")),
    url(r'^book/',include("bookings.urls",namespace="book")),
    #url(r'^api/venue/',CityListApiView.as_view())
    url(r'^',include("search.urls",namespace="search")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)