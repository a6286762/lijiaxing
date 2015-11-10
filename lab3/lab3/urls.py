# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from books import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# meiyoudedongxier
# duodade
# woyoulaigaile
urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
                
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    #(r'^',views.search),
    (r'^search-form/$',views.search_form),
    (r'^search/$',views.search),
    (r'^look/$',views.look),
    (r'^delete/$',views.delete),
)
