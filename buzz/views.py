from django.shortcuts import render
import requests
import json

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        data={}
        data['username']=username
        data['password']=password
        url=''
        api=requests.post(url=url,json=data)
        try:
            api_data=json.loads(api)
        except:
            api_data="error"
        tokens=api_data.token
    
    return render(request,'login.html')

