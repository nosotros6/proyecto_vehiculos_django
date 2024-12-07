from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login
from django.template import TemplateDoesNotExist
# Local
from .forms import RegistroUsuarioForm


# Create your views here.
def registro_view(request):
    try:
        if request.method == "POST":
            form = RegistroUsuarioForm(request.POST) 
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registrado Satisfactoriamente.")
                return HttpResponseRedirect('/menu') 
            messages.error(request, "Registro inválido. Algunos datos ingresados no son correctos.")
        
        form = RegistroUsuarioForm()
        return render(request, "usuario/registro.html", {"registro_form": form})
    
    except TemplateDoesNotExist as e:
        # Muestra un mensaje en caso de que la plantilla no sea encontrada
        return HttpResponse(f"Plantilla no encontrada: {e}")
    
    # Vista para login
def login_view(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Inicio de sesión exitoso.")
                return HttpResponseRedirect('/menu')  # Cambia '/menu' por tu página principal
            else:
                messages.error(request, "Credenciales inválidas. Por favor, intente de nuevo.")
        
        return render(request, "usuario/login.html")
    
    except TemplateDoesNotExist as e:
        return HttpResponse(f"Plantilla no encontrada: {e}")

