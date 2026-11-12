from django.shortcuts import render
from .forms import GeneradorForm
from .utils import construir_grupos, evaluar_fortaleza, generar_clave

def generador(request):
    form = GeneradorForm(request.GET or None)
    claves = []
    fortaleza = None

    if form.is_valid():
        datos = form.cleaned_data
        grupos = construir_grupos(
            datos["minusculas"], datos["mayusculas"],
            datos["numeros"], datos["simbolos"],
        )

        claves = [generar_clave(datos["longitud"], grupos)
            for _ in range(5)]
        fortaleza = evaluar_fortaleza(
            datos["longitud"], len("".join(grupos))
        )
    contexto = {"form": form, "claves": claves, "fortaleza": fortaleza}
    return render(request, "generador/generador.html", contexto)
