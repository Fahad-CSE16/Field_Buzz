from django.shortcuts import redirect, render
import requests
import json
import uuid
import time
from .forms import SubmitForm
from django.contrib import messages
def payload(request):
    if request.method=="POST":
        url='https://recruitment.fisdev.com/api/login/'
        jsons={"username":"mdfahadhossain71@gmail.com","password":"b0GmBmi57"}
        api=requests.post(url,json=jsons)
        try:
            resp=json.loads(api.text)
        except:
            resp=None
        if resp:
            token=resp['token']
        millis = int(round(time.time() * 1000))

        id=uuid.uuid4()
        id2=uuid.uuid4()
        id2s=str(id2)
        form=SubmitForm(request.POST, request.FILES)
        url2= 'https://recruitment.fisdev.com/api/v0/recruiting-entities/'
        if form.is_valid():
            jsons2={
                "tsync_id":str(id),
                "name":form.data['name'],
                "email":form.data['email'],
                "phone":form.data['phone'],
                "full_address":form.data['full_address'],
                "name_of_university":form.data['name_of_university'],
                "graduation_year":form.data['graduation_year'],
                "cgpa":form.data['cgpa'],
                "experience_in_months":form.data['experience_in_months'],
                "current_work_place_name":form.data['current_work_place_name'],
                "applying_in":form.data['applying_in'],
                "expected_salary":form.data['expected_salary'],
                "field_buzz_reference":form.data['field_buzz_reference'],
                "github_project_url":form.data['github_project_url'],
                "cv_file":{"tsync_id":id2s},
                "on_spot_update_time":millis,
            }
            api2=requests.post(url2,json=jsons2,headers={'Authorization':f'token {token}'})
            try:
                resp1=json.loads(api2.text)
            except:
                resp1=None
            if resp1:
                cv_file2=resp1['cv_file']['id']
            url3=f'https://recruitment.fisdev.com/api/file-object/{cv_file2}/'
            myfiles={'file': request.FILES['cv_file']}
            api3=requests.get(url3,files = myfiles,headers={'Authorization':f'token {token}','Content_type':'application/pdf'})
            try:
                resp2=json.loads(api3.text)
            except:
                resp2=None
            print(resp2)
            if resp2:
                messages.success(request,"Successfully submitted your Data!")
                messages.success(request,resp2)
            return redirect('home')
    else:
        form=SubmitForm()
    return render(request,'payload.html',{'form':form})
