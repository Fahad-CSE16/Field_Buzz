from django import forms
import os
 
from django.core.exceptions import ValidationError
class SubmitForm(forms.Form):
    CATEGORY=[
        ('Mobile','Mobile'),
        ('Backend','Backend'),
    ]
    # CATEGORY=('teacher','student')
    name=forms.CharField(max_length=256,required=True)
    email=forms.EmailField(required=True)
    phone=forms.CharField(max_length=14,required=True)
    full_address=forms.CharField(max_length=512,required=False)
    name_of_university=forms.CharField(max_length=256,required=True)
    graduation_year=forms.IntegerField(max_value=2020, min_value=2015, required=True)
    cgpa =forms.FloatField(max_value=4,min_value=2,required=False)
    experience_in_months = forms.IntegerField(max_value=100, min_value=0,required=False)
    current_work_place_name = forms.CharField(max_length=256,required=False)
    applying_in=forms.ChoiceField(choices=CATEGORY, required=True)
    expected_salary=forms.IntegerField(max_value=60000,min_value=15000,required=True)
    field_buzz_reference=forms.CharField(max_length=256,required=False)
    github_project_url =forms.URLField(max_length=512,required=True)
    cv_file=forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    # def clean_cv_file(self):
    #     print('any')
    #     cv_file = self.cleaned_data.get('cv_file',True)
    #     if cv_file:
    #         print(os.path.getsize(cv_file))
    #         if cv_file.size > 4*1024*1024:
    #             raise ValidationError("File size is too large ( > 4mb )")
    #         return cv_file
    #     else:
    #         raise ValidationError("Couldn't read uploaded image")



   