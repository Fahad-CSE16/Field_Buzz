from django.urls import path,include
from .views import signin
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', signin),
    path('',TemplateView.as_view(template_name='home.html')),
]