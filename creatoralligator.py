from Render import Render, color
from  ModelObj import *
from ShaderGL import *

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020
Lab 01 Filling a polygon 
"""

########################### Lista de colores para probar
Fondo = color(0,0,0) #negro
Blanco = color(1,1,1)
CYAN = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)

###########################################################
# tamaño de la imagen
prueba = Render(1080,720)
# introduzca el tamaño del viewport
#prueba.glViewport(500, 150, 200 ,400)

# ingrese el color del fondo
#prueba.glClearColor(0,0,0)

# ingrese el color para pintar

prueba.glClear()

######################Punto ##################################
# si quiere pintar un punto es aqui
#prueba.punto(150,275)
#prueba.glColor(1,0,0)
#prueba.punto(100,200)

# quiere pintar una linea, perfecto! aca es el espacio
#prueba.glLinea(-1,1, 1,-1)
#prueba.glLinea(-1,-1,1,1)
#prueba.glLinea(1,0,-1,-1)
#prueba.glLinea(1,-1,1,1)


#################### Model Obj #############################################

#fondo = Texture('./modelos/714138.bmp')
#prueba.FondoBMP(fondo.pixels)



#prueba.active_shader =  cartoonshader
prueba.luz = (0, 0, 1)


#               X Y Z     POsicion Camara
prueba.lookAt((0,0,-10), (1,1,6))

#prueba.active_texture =  Texture('./modelos/color.bmp')
                                            # X  Y Z      # Escala           # muevo roto scalo
#prueba.generacionObj('./modelos/paloma.obj',  (-2,2,-5), (0.28,0.28,0.28), (0,-45,0))

#prueba.active_texture =  Texture('./modelos/Char_Patrick.bmp')
#prueba.generacionObj('./modelos/patrick.obj',  (-2,2.5, -5), (0.8,0.8,0.8), (0,-45,0))
#2

#prueba.active_texture =  Texture('./modelos/Lizardtext.bmp')
#prueba.generacionObj('./modelos/Charizard.obj',  (-7,3,-6), (0.1,0.1,0.1), (0,90,0))






#prueba.active_texture =  Texture('./modelos/castillo.bmp')
#prueba.generacionObj('./modelos/Castilloobj.obj',  (-7,-4,-6), (0.005,0.005,0.005), (-90,0,45))

#prueba.active_texture =  Texture('./modelos/fire.bmp')
#prueba.generacionObj('./modelos/monster.obj',  (3,-4,-6), (0.0004,0.0004,0.0004), (0,-45,0))
prueba.glFinish('Sphere.bmp')







#################################  REFILL DE OBJTS




#prueba.glFinish('Poligono.bmp')


