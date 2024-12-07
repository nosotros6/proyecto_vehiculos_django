from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
# local Django
from .forms import VehiculoForm

# Create your views here.
class IndexPageView(TemplateView):
    template_name = "index.html"
   
#El parámetro `request` de esta fx, es un objeto que representa la solicitud HTTP que se está procesando. 
def vehiculoform_view(request): 
    # crea un diccionario vacío 'context' para almacenar datos al html q se renderiza al final
    context ={}
    # crea objecto formularo llamado 'form' para validar y procesar los datos.
    # El form se instancia con los datos q se envian a/t de la solicitud HTTP (request.POST y request.FILES).
    form = VehiculoForm(request.POST or None, request.FILES or None)
    
    # verifica si los datos del formulario son válidos. 
    # Si el formulario es válido, se ejecuta el código que se encuentra dentro de este bloque `if`.
    if form.is_valid():
        # Si es válido, guarda los datos del formulario en la base de datos (save the form data to model)
        form.save()
        #Si es válido, redirige al usuario a la página principal del sitio web (`/`).
        return HttpResponseRedirect('/') 
    #Si es válido, agrega el formulario a la variable `context`, que se pasará a la plantilla HTML.
    context['form']= form
    #renderiza la plantilla HTML `vehiculo_add_form.html` con los datos de la variable `context`,
    # y devuelve la respuesta HTTP al usuario.
    return render(request, "vehiculo_add_form.html", context)

def navbarView(request):
    template_name = 'navbar.html'
    return render(request, template_name)