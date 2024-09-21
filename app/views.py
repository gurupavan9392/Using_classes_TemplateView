from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse


class senddatabyTV(TemplateView):
    template_name='senddatabyTV.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='pavan'
        ECDO['age']=22
        ECDO['ECDO']=StudentForm()
        return ECDO
    
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')