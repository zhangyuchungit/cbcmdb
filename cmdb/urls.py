#-*- coding: utf-8 -*-
'''
    Author: smallmi
    Blog: http://www.smallmi.com
'''

"""skyoms URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from cmdb import views
from django.conf.urls import url,include

urlpatterns = [

    url(r'^index/$', views.Index, name='Index'),
    url(r'^order/$', views.order, name='order'),
    url(r'^cate/$', views.cate, name='cate'),
    url(r'^projectname/$', views.projectname, name='projectname'),
    url(r'^adminlist/$', views.adminlist, name='adminlist'),
    url(r'^addproject/$', views.addproject, name='addproject'),
    url(r'^hostadd/$', views.hostadd, name='hostadd'),
    url(r'^currentpage/$', views.currentpage, name='currentpage'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^view/$', views.view, name='view'),
    url(r'^svninfo/$', views.svninfo, name='svninfo'),
    url(r'^svninfoadd/$', views.svninfoadd, name='svninfoadd'),
    url(r'^svninfoedit/$', views.svninfoedit, name='svninfoedit'),
    url(r'^projectview/$', views.projectview, name='projectview'),


]
