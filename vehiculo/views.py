from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
# local Django
from .forms import VehiculoForm

# Create your views here.
class IndexPageView(TemplateView):
    template_name = "index.html"
    
def vehiculoform_view(request): 
    context ={}
    # create object of form
    form = VehiculoForm(request.POST or None, request.FILES or None)
    
    # check if form data is valid
    if form.is_valid():
        # save the form data to model 
        form.save()
        return HttpResponseRedirect('/')
    context['form']= form
    return render(request, "vehiculo_add_form.html", context)

def navbarView(request):
    template_name = 'navbar.html'
    return render(request, template_name)