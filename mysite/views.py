from django.http import HttpResponse, Http404
from  django.template import Template, Context
import  datetime, requests
from django.template.loader import get_template
from django.template import Template,Context
from django.shortcuts import render

def hello(request):
    return HttpResponse ("Hello world")

def current_datetime(request):
    now =datetime.datetime.now()
    html = "<html><body>%s<body/><html/>" % now
    return  HttpResponse(html)


def current_datetime2(request):
    now =datetime.datetime.now()
    t = Template("<html><body> {{ current_date }} <body/><html/>")
    html = t.render(Context({'current_date':now}))
    return  HttpResponse(html)


def current_datetime3(request):
    now =datetime.datetime.now()
    fp = open("D:/web_devlopment_study/Django/django_project/env_mysite/Scripts/mysite/template/mytemplate.html")
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date':now}))
    return  HttpResponse(html)

def current_datetime4(request):
    now =datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date':now}))
    return  HttpResponse(html)

def current_datetime5(request):
    now =datetime.datetime.now()
    return  render(request,'current_datetime.html',{'current_date':now})

def current_datetime6(request):
    now =datetime.datetime.now()
    return  render(request,'includes/mypage.html',{'current_date':now, 'title':'Norway time'})

def current_datetime7(request):
    now =datetime.datetime.now()
    return  render(request,'current_datetime_new.html',{'current_date':now, 'title':'Norway'})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours= offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_ahead2(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours= offset)
    return render(request,'hours_ahead.html',{'hour_offset':offset,'next_time': dt })

def get_wms_viz(requets):
    url = "http://geo.vliz.be/geoserver/MarineRegions/wms?REQUEST=GetFeatureInfo&SERVICE=WMS&SRS=EPSG%3A4326&STYLES=&BUFFER=10&TRANSPARENT=true&VERSION=1.1.1&FORMAT=image%2Fpng&BBOX=-52.82226562499999%2C-39.0277188402116%2C116.103515625%2C35.53222622770337&HEIGHT=916&WIDTH=1922&LAYERS=MarineRegions%3Aeez&QUERY_LAYERS=MarineRegions%3Aeez&INFO_FORMAT=application%2Fjson&X=1222&Y=515";
    f = requests.get(url)
    html = "<html><body>%s<body/><html/>" % f.text
    return  HttpResponse(html)

def current_url_view_good(request):
    print("Comments######### " + str(request.META))
    return HttpResponse("Welcome to the page at %s" % request.META)



