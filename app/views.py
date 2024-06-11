from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
class DataInsertByTV(TemplateView):
    template_name='DataInsertByTV.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        #ECDO['name']='ASHU'
        #ECDO['age']=3

        ECDO['ECFO']=CollegeForm()
        return ECDO
    def post(self,request):
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('DataInsertByTV is done')
        else:
            return HttpResponse('DataInsertByTV not done')


class InsertDataByFv(FormView):
    template_name='InsertDataByFv.html'
    form_class=CollegeForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('DONE')