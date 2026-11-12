import math
import secrets
import string

SIMBOLOS = "!@#$%&*?-_+="

def construir_grupos(minusculas, mayusculas, numeros, simbolos):
    """Devuelve la lista de grupos de caracteres elegidos."""
    grupos = []
    if minusculas:
        grupos.append(string.ascii_lowercase)
    if mayusculas:
        grupos.append(string.ascii_uppercase)
    if numeros:
        grupos.append(string.digits)
    if simbolos:
        grupos.append(SIMBOLOS)

    return grupos

def generar_clave(longitud, grupos):
    """Genera una clave con al menos un carácter de cada grupo."""
    alfabeto = "".join(grupos)
    caracteres = [secrets.choice(grupo) for grupo in grupos]
    while len(caracteres) < longitud:
        caracteres.append(secrets.choice(alfabeto))
    secrets.SystemRandom().shuffle(caracteres)
    return "".join(caracteres)

def evaluar_fortaleza(longitud, tam_alfabeto):
    """Estima la entropía en bits y la traduce a un nivel."""
    bits = round(longitud * math.log2(tam_alfabeto))
    if bits < 50:
        nivel, color = "Débil", "#e74c3c"
    elif bits < 80:
        nivel, color = "Aceptable", "#f39c12"
    elif bits < 110:
        nivel, color = "Fuerte", "#27ae60"
    else:
        nivel, color = "Blindada", "#2e86de"

    porcentaje = min(100, round(bits / 128 * 100))
    return {"bits": bits, "nivel": nivel, "color": color,
        "porcentaje": porcentaje}