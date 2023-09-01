from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    QSTO=topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def insert_topic(request):
    tn=input('enter topic name: ')
    TO=topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    QSTO=topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def insert_webpage(request):
    tn=input('enter topic name: ')
    wn=input('enter name: ')
    ur=input('enter url: ')
    TO=topic.objects.get(topic_name=tn)
    WO=webpage.objects.get_or_create(topic_name=TO,name=wn,url=ur)[0]
    WO.save()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)



def display_accessrecords(request):
    QSARO = AccessRecord.objects.all()
    d = {'QSARO': QSARO}
    return render(request, 'display_accessrecords.html', d)


def Insert_accessrecord(request):
    wn=input('enter name: ')
    WO=webpage.objects.get(name=wn)
    d=input('enter date : ')
    a=input('enter author : ')
    e=input('enter email : ')
    ao=AccessRecord.objects.get_or_create(name=WO,date=d,author=a,email=e)[0]
    ao.save()
    QSARO = AccessRecord.objects.all()
    d = {'QSARO': QSARO}
    return render(request, 'display_accessrecords.html', d)