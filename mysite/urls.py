"""mysite URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello,current_datetime, hours_ahead,get_wms_viz,current_datetime2,current_datetime3,current_datetime4,current_datetime5,current_datetime6,current_datetime7,hours_ahead2,current_url_view_good



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time2/$', current_datetime2),
    url(r'^time3/$', current_datetime3),
    url(r'^time4/$', current_datetime4),
    url(r'^time5/$', current_datetime5),
    url(r'^time6/$', current_datetime6),
    url(r'^time7/$', current_datetime7),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^time/pluss/(\d{1,2})/$', hours_ahead2),
    url(r'^viz/$', get_wms_viz),
    url(r'^weburl/$', current_url_view_good),

]
