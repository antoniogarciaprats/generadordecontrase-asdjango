from django import forms

# Creamos el formulario para el proyecto
class GeneradorForm(forms.Form):
    longitud = forms.IntegerField(
        label="Longitud", min_value=6, max_value=64, initial=16
    )
    minusculas = forms.BooleanField(
        label="Minúsculas (a-z)", required=False, initial=True
    )
    mayusculas = forms.BooleanField(
        label="Mayúsculas (A-Z)", required=False, initial=True
    )
    numeros = forms.BooleanField(
        label="Números (0-9)", required=False, initial=True
    )
    simbolos = forms.BooleanField(
        label="Símbolos (!@#$…)", required=False
    )

    def clean(self):
        datos = super().clean()
        tipos = ("minusculas", "mayusculas", "numeros", "simbolos")

        # Validamos que al menos una casilla de tipo de carácter esté marcada
        if not any(datos.get(tipo) for tipo in tipos):
            raise forms.ValidationError("Marca al menos un tipo de caracter")

        return datos