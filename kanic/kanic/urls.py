"""kanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

# from users.serializers import UserViewSet, MechanicViewSet
# from requests.serializers import RequestViewSet, ServiceViewSet
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView
from requests.views import (RequestRetrieveAPIView, RequestCreateAPIView,
RequestListAPIView, ServiceListAPIView, ServiceRetrieveAPIView)

# router = routers.DefaultRouter()
# router.register(r'mechanics', MechanicViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'services', ServiceViewSet)
# router.register(r'requests', RequestViewSet)

from kanic import views

urlpatterns = [

    # api URLs
    url(r'^api-beta/auth/token/?$', 'rest_framework_jwt.views.obtain_jwt_token'),

    # include api/auth/login and api/auth/logout
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/', include(router.urls)),

    # users
    url(r'^api-beta/users/?$', UserListAPIView.as_view(), name='user_list_api'),
    url(r'^api-beta/users/create/?$', UserCreateAPIView.as_view(), name='user_create_api'),
    url(r'^api-beta/users/(?P<username>[\w-]+)/?$', UserRetrieveAPIView.as_view(), name='user_retrieve_api'),

    # car owners
    # url(r'^api-beta/car-owners/?$', CarOwnerListAPIView.as_view(), name='car_onwer_list_api'),
    # url(r'^api-beta/car-owners/(?P<username>[\w-]+)/?$', CarOwnerRetrieveAPIView.as_view(), name='car_owner_retrieve_api'),

    # services
    url(r'^api-beta/services/?$', ServiceListAPIView.as_view(), name='service_list_api'),
    # url(r'^api-beta/services/create/?$', ServiceCreateAPIView.as_view(), name='user_create_api'),
    url(r'^api-beta/services/(?P<id>[\w-]+)/?$', ServiceRetrieveAPIView.as_view(), name='service_retrieve_api'),

    # requests
    url(r'^api-beta/requests/?$', RequestListAPIView.as_view(), name='request_list_api'),
    url(r'^api-beta/requests/create/?$', RequestCreateAPIView.as_view(), name='request_create_api'),
    url(r'^api-beta/requests/(?P<id>[\w-]+)/?$', RequestRetrieveAPIView.as_view(), name='request_retrieve_api'),

    # django-registration-redux URLs
    # url(r'^accounts/', include('registration.backends.default.urls')),

    # web-based URLs
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^home', views.home, name='home'),

    # testing URLs
    url(r'^testform', views.testform),



]
