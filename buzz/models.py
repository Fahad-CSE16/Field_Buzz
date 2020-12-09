# from django.db import models

# # Create your models here.
# class SubmitForm(models.Model):
#     CATEGORY=[
#         ('Mobile','Mobile'),
#         ('Backend','Backend'),
#     ]
#     # CATEGORY=('teacher','student')
#     name=models.CharField(max_length=256,required=True)
#     email=models.EmailField(required=True)
#     phone=models.CharField(max_length=14,required=True)
#     full_address=models.CharField(max_length=512,required=False)
#     name_of_university=models.CharField(max_length=256,required=True)
#     graduation_year=models.IntegerField(max_value=2020, min_value=2015, required=True)
#     cgpa =models.FloatField(max_value=4,min_value=2,required=False)
#     experience_in_months = models.IntegerField(max_value=100, min_value=0,required=False)
#     current_work_place_name = models.CharField(max_length=256,required=False)
#     applying_in=models.ChoiceField(choices=CATEGORY, required=True)
#     expected_salary=models.IntegerField(max_value=60000,min_value=15000,required=True)
#     field_buzz_reference=models.CharField(max_length=256,required=False)
#     github_project_url =models.URLField(max_length=512,required=True)
#     cv_file=models.FileField(widget=models.FileInput(attrs={'accept':'application/pdf'}))
#     # def clean_cv_file(self):
#     #     print('any')
#     #     cv_file = self.cleaned_data.get('cv_file',True)
#     #     if cv_file:
#     #         print(os.path.getsize(cv_file))
#     #         if cv_file.size > 4*1024*1024:
#     #             raise ValidationError("File size is too large ( > 4mb )")
#     #         return cv_file
#     #     else:
#     #         raise ValidationError("Couldn't read uploaded image")



   