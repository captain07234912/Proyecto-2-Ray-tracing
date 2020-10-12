from LibreriaGL import  *

import random
import struct
from numpy import matrix, cos, sin, tan
from ModelObj import *

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020

Shaders de la clase y los propios 

"""


# ejemplo de clase
def gourad(render, **kwargs):

    # baricentricas
    u, v, w = kwargs['baryCoords']
    # textura
    ta, tb, tc = kwargs['texCoords']

    #normal

    na, nb, nc = kwargs['normals']
    #colores
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255



    # si hay textura hay playa, si hay playa , hay alcohol


    if render.active_texture:

        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    # como en el  SR4
    intensidad =  productopunto(normal, render.luz)

    b *= intensidad
    g *= intensidad
    r *= intensidad

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0





# implementacion del toon shader
def cartoonshader(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    ta, tb, tc = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w
        TColor = render.active_texture.getColor(tx, ty)
        b *= TColor[0] / 255
        g *= TColor[1] / 255
        r *= TColor[2] / 255

    Normalx = na[0] * u + nb[0] * v + nc[0] * w
    Normaly = na[1] * u + nb[1] * v + nc[1] * w
    Normalz = na[2] * u + nb[2] * v + nc[2] * w
    normal = (Normalx, Normaly, Normalz)
    intensity = productopunto(normal, render.luz)

    # cuatro sombras toon 0-100
    if intensity < 0:
        intensity = 0
    elif intensity < 0.26:
        intensity = 0.25
    elif intensity < 0.51:
        intensity = 0.50
    elif intensity < 0.76:
        intensity = 0.75
    elif intensity < 1.0:
        intensity = 0.99
    elif intensity > 1.0:
        intensity = 1
    else:
        intensity = 0

    # con textura
    if render.active_texture:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w

        TColor = render.active_texture.getColor(tx, ty)

        b *= TColor[0] / 255

        g *= TColor[1] / 255
        r *= TColor[2] / 255

    b *= intensity
    g *= intensity
    r *= intensity

    return r, g, b

# shader gradiente de color
def cartoonshadess(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    ta, tb, tc = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w
        TColor = render.active_texture.getColor(tx, ty)
        b *= TColor[0] / 255
        print(TColor)
        g *= TColor[1] / 255
        r *= TColor[2] / 255

    Normalx = na[0] * u + nb[0] * v + nc[0] * w
    Normaly = na[1] * u + nb[1] * v + nc[1] * w
    Normalz = na[2] * u + nb[2] * v + nc[2] * w
    normal = (Normalx, Normaly, Normalz)
    intensity = productopunto(normal, render.luz)

    # cuatro sombras toon 0-100
    if intensity < 0:
        intensity = 0

    elif intensity < 0.26:
        intensity = 0.25

    elif intensity < 0.51:
        intensity = 0.50

    elif intensity < 0.76:
        intensity = 0.75
    elif intensity < 1.0:
        intensity = 0.99
    elif intensity > 1.0:
        intensity = 1.5
    else:
        intensity = 0



    b *= intensity
    g *= intensity
    r *= intensity

    return r, g, b

# shader
