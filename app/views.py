from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
 
def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QST=Topic.objects.all()
    d={'topics':QST}

    if request.method=='POST':
        topic=request.POST.get('topic')
        na=request.POST['na']
        ur=request.POST.get('ur')
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        w=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        w.save()
        return HttpResponse('webpage is created')
    return render(request,'insert_webpage.html',d)


