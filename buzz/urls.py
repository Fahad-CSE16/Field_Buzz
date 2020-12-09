from django.urls import path
from .views import payload
from django.views.generic import TemplateView

urlpatterns = [
    path('payload/', payload),
    path('',TemplateView.as_view(template_name='home.html'), name='home'),
]