from Render import Render, color
from  ModelObj import *
from ShaderGL import *
from Sphere import *
"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293

18/10/2020


Proyecto No. 2 Ray Tracing

"""

########################### Lista de colores para probar
Fondo = color(0,0,0) #negro
Blanco = color(1,1,1)
CYAN = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)

###########################################################

brick = Material(diffuse = color(0.8, 0.25, 0.25 ), spec = 32, matType = REFLECTIVE)
stone = Material(diffuse = color(0.4, 0.4, 0.4 ), spec = 32)
mirror = Material(spec = 64, matType = REFLECTIVE)
glass = Material(spec = 64, ior = 1.5, matType= TRANSPARENT)


width = 520
height = 320
prueba = Render(width, height)
prueba.glClearColor(0.2, 0.6, 0.8)
prueba.glClear()



# Lights
prueba.pointLights.append(PointLight(position = (-4, 20, 0), intensity = 0.5))
prueba.pointLights.append(PointLight(position = (4, -20, 0), intensity = 0.5))
prueba.dirLight = DirectionalLight(direction =(1, -2, -2), intensity = 0.5)
prueba.ambientLight = AmbientLight(strength = 0.1)

prueba.envmap = Envmap('text/sape6.bmp')
#r.scene.append( Sphere(( 0, 0, -8), 2, earthMat))

###########################################################

############################################################################################Mesa ############################################
grama = Material(texture = Texture('text/telasampo.bmp'))



madera = Material(texture = Texture('text/enma.bmp'))

palo = Material(texture = Texture('text/rojote.bmp'))

madera2 = Material(texture = Texture('text/madera2.bmp'))

cuadro1 =  Material(texture = Texture('text/perro3.bmp'))
cuadro2 =  Material(texture = Texture('text/perro4.bmp'))

palobillar = Material(texture = Texture('text/palobillar.bmp'))


prueba.scene.append(AABB(position=(0, 7, -35), size = (20, 1, 35), material = grama))
prueba.scene.append(AABB(position=(0, 7.5, -16), size = (20, 2, 1), material = madera))
prueba.scene.append(AABB(position=(10, 7.5, -35), size = (1, 2, 37), material = madera))
prueba.scene.append(AABB(position=(-10, 7.5, -35), size = (1, 2, 37), material = madera))
prueba.scene.append(AABB(position=(0, 7.5, -54), size = (20, 2, 1), material = madera))
prueba.scene.append(AABB(position=(9, 4.3, -19), size = (2, 5, 2), material = madera))
prueba.scene.append(AABB(position=(-9, 4.3, -19), size = (2, 5, 2), material = madera))
"""
########################## BOLAS #################################
#Fila 5

ballMat11 = Material(texture = Texture('text/ball11.bmp'))
ballMat12 = Material(texture = Texture('text/ball12.bmp'))
ballMat13 = Material(texture = Texture('text/ball13.bmp'))
ballMat14 = Material(texture = Texture('text/ball14.bmp'))
ballMat15 = Material(texture = Texture('text/ball15.bmp'))

prueba.scene.append(Sphere((0, 8.30, -45), 0.8, ballMat11))
prueba.scene.append(Sphere((2, 8.30, -45), 0.8, ballMat12))
prueba.scene.append(Sphere((4, 8.30, -45), 0.8, ballMat13))
prueba.scene.append(Sphere((-2, 8.30, -45), 0.8, ballMat14))
prueba.scene.append(Sphere((-4, 8.30, -45), 0.8, ballMat15))

#Fila 4
ballMat7 = Material(texture = Texture('text/ball7.bmp'))
ballMat8 = Material(texture = Texture('text/ball8.bmp'))
ballMat9 = Material(texture = Texture('text/ball9.bmp'))
ballMat10 = Material(texture = Texture('text/ball10.bmp'))
prueba.scene.append(Sphere((1, 8.30, -40), 0.8, ballMat7))
prueba.scene.append(Sphere((-1, 8.30, -40), 0.8, ballMat8))
prueba.scene.append(Sphere((3, 8.30, -40), 0.8, ballMat9))
prueba.scene.append(Sphere((-3, 8.30, -40), 0.8, ballMat10))

#Fila 3
ballMat4 = Material(texture = Texture('text/ball5.bmp'))
ballMat5 = Material(texture = Texture('text/ball6.bmp'))
ballMat6 = Material(texture = Texture('text/ball7.bmp'))
prueba.scene.append(Sphere((0, 8.30, -35), 0.8, ballMat4))
prueba.scene.append(Sphere((2, 8.30, -35), 0.8, ballMat5))
prueba.scene.append(Sphere((-2, 8.30, -35), 0.8, ballMat6))

#Fila 2
ballMat2 = Material(texture = Texture('text/ball2.bmp'))
ballMat3 = Material(texture = Texture('text/ball3.bmp'))
prueba.scene.append(Sphere((1, 8.30, -30), 0.8, ballMat2))
prueba.scene.append(Sphere((-1, 8.30, -30), 0.8, ballMat3))

#Fila 1
ballMat1 = Material(texture = Texture('text/ball1.bmp'))
prueba.scene.append(Sphere((0, 8.30, -25), 0.8, ballMat1))

#Blanca
ballMatW = Material(texture = Texture('text/bball.bmp'))
prueba.scene.append(Sphere((0, 8.30, -18), 0.8, ballMatW))
"""
############### Cuadros ##################################
"""
prueba.scene.append(AABB(position=(-20, 24, -52), size = (38, 24, 1), material = cuadro1))
prueba.scene.append(AABB(position=(-20, 24, -54), size = (42, 28, 1), material = madera2))
prueba.scene.append(AABB(position=(26, 28, -54), size = (30, 20, 1), material = madera2))
prueba.scene.append(AABB(position=(26, 28, -53), size = (27, 18, 1), material = cuadro2))
"""
########################## Esfera reflectiva y retractiva #########################################################

prueba.scene.append(Sphere((0, 30, -40), 7, material = mirror))
prueba.scene.append(AABB(position=(0, 33, -49), size = (2, 18, 2), material = palo))
prueba.scene.append(AABB(position=(300, 10, -49), size = (2, 26, 1), material = palobillar))

prueba.rtRender()

#palo de billar



prueba.glFinish('output23.bmp')



