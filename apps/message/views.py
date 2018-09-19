from django.shortcuts import render
import pymysql
# Create your views here.

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
django.setup()

from .models import UserMessage




def getform(request):
    #all_messages = UserMessage.objects.all()
    #for message in all_messages:
     #   print (message.name)
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.adress = address
        user_message.email = email
        user_message.object_id = "helloworld3"
        user_message.save()



    return render(request,'message_form.html')