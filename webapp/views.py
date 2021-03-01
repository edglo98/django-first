from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from personas.models import Persona


def welcome(request):
    # no_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/
    # mensajes = {'response': no_personas}
    mensajes = {'usuario': 'edgar', 'response': [{'id': 1, 'nombre': 'edgar'}, {'id': 2, 'nombre': 'freddy'}, {'id': 3, 'nombre': 'lizbeth'}, {'id': 4, 'nombre': 'mario'}]}
    return render(request, 'welcome.html', mensajes)


def bye(request):
    return HttpResponse('<h1>adiosito</h1>')


def contact(request):
    return HttpResponse('<h1>contactame</h1>')


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    # persona = get_object_or_404(Persona, pk=id)

    return render(request, 'personas/detalle_persona.html', {'id': id})
