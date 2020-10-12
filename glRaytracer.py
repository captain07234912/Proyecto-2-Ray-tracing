from LibreriaGL import *
from ModelObj import *
from Sphere import  Sphere, Material, Light
from Render import Render
import random

"""
Universidad del Valle de Guatemala
Graficas por computadora
Raytracing
Jorge Suchite Carnet 15293
07/09/2020

DR1 Spheraes and materials

"""

############################# SNOWMAN ###########################################

###################################################Materiales ##############################
negro = Material(diffuse= color(0,0,0))
naranja = Material(diffuse=color(0.92,0.56,0.12))
Snow = Material(diffuse=color(1,1,1))
Azulado = Material(diffuse= color(0,0,1))

#################################################################################

width = 700
height = 700

prueba = Render(width,height)
prueba.light= Light(position = (-5,5,0), intensity= 1.5)


# pa que corra todo junto y no separado

        #      coordenada x,y,z radio , material
prueba.scene = [Sphere((0,1,-10),1.5,Snow),
             Sphere((0,3.2,-10),1, Snow),
             Sphere((0,-2,-10),2,Snow),
                Sphere((0, 3, -9),0.2, naranja),
Sphere((0.5, 3.2, -9),0.15, negro),
Sphere((-0.5, 3.2, -9),0.15, negro),
Sphere((-0.5,2.5, -9),0.10,negro),
Sphere((0.5,2.5, -9),0.10,negro),
Sphere((0,2.5, -9),0.10,negro),
Sphere((0.25,2.5, -9),0.10,negro),
Sphere((-0.25,2.5, -9),0.10,negro),

Sphere((0,-0.7, -8),0.3,negro),
Sphere((0,0.5, -8),0.22,negro),
Sphere((0,1.5, -8),0.2,negro),




                ]



prueba.rtRender()


prueba.glFinish('Snowman23.bmp')