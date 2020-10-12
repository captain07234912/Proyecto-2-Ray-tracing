import struct
from LibreriaGL import *
from ModelObj import *
from Sphere import *
import numpy as np

from Sphere import Intersect

from numpy import matrix, cos, sin, tan
"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020
Fill a polygon 
"""


BLACK = color(0,0,0)
class Render(object):
    def __init__(self, width, height):
        self.colorPintar = Blanco
        self.Fondo = BLACK
        self.glCreateWindow(width, height)
        # ancho y largo de la imagen
        self.camPosition = (0, 0, 0)
        self.fov = 60
        self.scene =[]

        self.pointlight = None

        #luz de direccion




        # matriz de la cmaara igual que la del obj

    def createViewMatrix(self, camPosition=(0, 0, 0), camRotation=(0, 0, 0)):


        camMatrix = self.createObjectMatrix(translate=camPosition, rotate=camRotation)

            # inversa en libreria gl
        self.viewMatrix = Inversa(camMatrix)


        #funcion lookat
    def lookAt(self, eye, camPosition=(0, 0, 0)):
         # magnitud del vector
         # magnum en LIbreria GL
        forward = magnum(camPosition, eye)

        forward =  normal(forward)

        right = productocruz((0, 1, 0), forward)
        right =  normal(right)

        up = productocruz(forward, right)
        up = normal(up)

        camMatrix = [[right[0], up[0], forward[0], camPosition[0]],
                            [right[1], up[1], forward[1], camPosition[1]],
                            [right[2], up[2], forward[2], camPosition[2]],
                            [0, 0, 0, 1]]

        self.viewMatrix =  Inversa(camMatrix)

    def createProjectionMatrix(self, n=0.1, f=1000, fov=60):

        t = tan((fov * valorpi / 180) / 2) * n
        r = t * self.ViewportWidth / self.ViewportHEight

        self.projectionMatrix = [[n / r, 0, 0, 0],
                                        [0, n / t, 0, 0],
                                        [0, 0, -(f + n) / (f - n), -(2 * f * n) / (f - n)],
                                        [0, 0, -1, 0]]

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

        #tamani exacto de la ventana
        self.glViewport(0, 0, width, height)

    """
    define el area  de la imagen sobre la que vas a dibujar
    """
    def glViewport(self, x, y, width, height):
        self.CoorxViewport = x
        self.CooryViewport = y
        self.ViewportHEight = height
        self.ViewportWidth = width

        self.viewportMatrix =[[width / 2, 0, 0, x + width / 2],
                                      [0, height / 2, 0, y + height / 2],
                                      [0, 0, 0.5, 0.5],
                                      [0, 0, 0, 1]]

    """funcion que llena toda la imagen de un solo color con pixeles   
         tomando la imagen como una matriz papu"""
    def glClear(self):
        self.pixels = [[self.Fondo for x in range(self.width)] for y in range(self.height)]
        self.zbuffer = [[float('inf') for x in range(self.width)] for y in range(self.height)]

    # funcion que me deeja ahcer el punto x largo y  alto
    # si lo pinta mitad afuera y mitad adentro puedo verlo
    def punto(self,x,y, _color= None):
        try:
            self.pixels[y][x] = _color
        except:
            pass


    """ https://www.khronos.org/registry/OpenGL-Refpages/es2.0/xhtml/glViewport.xml
    
        link donde se utilizo la formula para el viewport"""
    # vertex relativo al viewport punto en pantalla conversion valor en pixel
    def glVertex(self, x, y,   ):
        pixelX =  int(( x + 1) * (self.ViewportWidth / 2) + self.CoorxViewport)
        pixelY =  int(( y + 1) * (self.ViewportHEight / 2) + self.CooryViewport)
        self.pixels[pixelY][pixelX] = self.colorPintar
    def glvertexLinea(self,xcoor,ycoor):
# si se pasa del rango puedo ver si si lo pinta o no
        try:
            self.pixels[ycoor][xcoor] = self.colorPintar
        except:
            pass

    def glVertex_coord(self, x, y, _color=None):
        if x < self.CoorxViewport or x >= self.CoorxViewport + self.ViewportWidth or y < self.CooryViewport or y >= self.CooryViewport + self.ViewportHEight:
            return

        if x >= self.width or x < 0 or y >= self.height or y < 0:
            return
        try:
            self.pixels[y][x] = _color or  self.colorPintar
        except:
            pass


    # j balvin men
    # este colores me sirve para guardar el color
    def glColor(self, r, g, b):
        self.colorPintar = color(r, g, b)
    # poner el color de fondo si quiere cuas

    def glClearColor(self, r, g, b):
        self.Fondo = color(r, g, b)
    # funcion que me deja escribir el BMP

    # aca termina lo de puntos

    ############################ Lineas ##################################
    ## algoritmo de bresenham dibujar una linea
    """https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""

    def glLinea(self, xi, yi, xn, yn ):
        # coordenadas iniciales y siguientes

        xi = round((xi+1) * (self.ViewportWidth/2 ) + self.CoorxViewport)
        yi = round((yi +1) * (self.ViewportHEight /2 ) + self.CooryViewport)
        xn = round((xn+1) * (self.ViewportWidth / 2) + self.CoorxViewport)
        yn = round((yn +1) * (self.ViewportHEight / 2 ) + self.CooryViewport)

    # distancias que se desplazan en cada eje calculando pendiente division por 0 =abs

        distx = abs(xn -xi)
        disty = abs(yn -yi)
        inclinacion = disty > distx
    # valores inclinados o rectos de 0 a 1

        if inclinacion:

            xi,yi = yi,xi
            xn,yn = yn,xn

        if xi > xn:
            xi,xn =xn,xi
            yi, yn = yn, yi

        distx = abs(xn-xi)

        disty = abs(yn -yi)

        moving = 0
        limite = 0.5
        m = disty/distx
        ycoor = yi

        # printeada de x
        for xcoor in range(xi, xn + 1):
            if inclinacion:
                self.glvertexLinea(ycoor,xcoor)
            else:
                self.glvertexLinea(xcoor,ycoor)
            # se le agrega valor de la pendiente a cada paso
            moving += m
            if moving >= limite:
                ycoor += 1 if yi < yn else -1
                limite += 1
    ####################  Linea algoritmoo de breseham pero en el las coordenadas de la ventana
    def glPrintLineaObj(self,xi,yi,xn,yn):
        dx = abs(xn - xi)
        dy = abs(yn - yi)

        steep = dy > dx

        if steep:
            xi, yi = yi, xi
            xn, yn = yn, xn

        if xi > xn:
            xi,xn =xn,xi
            yi, yn = yn, yi

        dx = abs(xn - xi)
        dy = abs(yn - yi)

        offset = 0
        limit = 0.5

        # como es un modelo en tres d cuando dibuja la tercera tiene division por 0 entonces, por el momento se desprecian

        try:
            m = dy/dx
        except ZeroDivisionError:
            pass
        else:
            y = yi

            for x in range(xi, xn + 1):
                if steep:
                    self.glvertexLinea(y, x)
                else:
                    self.glvertexLinea(x, y)

                offset += m
                if offset >= limit:
                    y += 1 if yi < yn else -1
                    limit += 1


    ########################## Modelo Obj ##################################

    def transform(self, vertex, vMatrix):

        #Matriz aumentada
        augVertex = [[vertex[0]],
                     [vertex[1]],
                     [vertex[2]],
                     [1]]

        #3 multiplicacion de matrices

        part1 = productomatriz(self.viewportMatrix, self.projectionMatrix)
        part2 = productomatriz(part1, self.viewMatrix)
        part3 = productomatriz(part2, vMatrix)

        transVertex = productomatriz(part3,augVertex)

        transVertex = (transVertex[0][0] / transVertex[3][0],
                        transVertex[1][0] / transVertex[3][0],
                        transVertex[2][0] / transVertex[3][0])
        #print(transVertex)
        return transVertex

    def dirTransform(self, vertex, dirMatrix):

        augVertex = [[vertex[0]],
                     [vertex[1]],
                     [vertex[2]],
                     [0]]

        transVertex = productomatriz(dirMatrix, augVertex)

        transVertex = (transVertex[0][0],
                       transVertex[1][0],
                       transVertex[2][0])

        return transVertex

    def createObjectMatrix(self, translate = (0,0,0), scale = (1,1,1), rotate=(0,0,0)):

        translacionMatriz = [[1, 0, 0, translate[0]],
                                  [0, 1, 0, translate[1]],
                                  [0, 0, 1, translate[2]],
                                  [0, 0, 0, 1]]

        scaleMatrix = [[scale[0], 0, 0, 0],
                              [0, scale[1], 0, 0],
                              [0, 0, scale[1], 0],
                              [0, 0, 0, 1]]

        rotacionMatriz = self.Matrizderotacion(rotate)


        multiXY = productomatriz(translacionMatriz, rotacionMatriz)
        #print(multiXY)

        multixyz = productomatriz(multiXY, scaleMatrix)
       # print(multixyz)

        return multixyz


        # sin, cos y tan liberados para usar de numpy




    def generacionObj(self, filename, translate = (0,0,0), scale = (1,1,1), rotate=(0,0,0)):
        model =ModelObJ(filename)

        modelMatrix = self.createObjectMatrix(translate, scale, rotate)

        rotationMatrix = self.Matrizderotacion(rotate)
        for caritas in model.faces:

            vertCount = len(caritas)

            """ 
            3 vertices de triangulos 
        
        
            """
            v0 = model.vertices[caritas[0][0] - 1]
            v1 = model.vertices[caritas[1][0] - 1]
            v2 = model.vertices[caritas[2][0] - 1]
            if vertCount > 3:
                v3 = model.vertices[caritas[3][0] - 1]
            v0 = self.transform(v0, modelMatrix)
            v1 = self.transform(v1, modelMatrix)
            v2 = self.transform(v2, modelMatrix)
            if vertCount > 3:
                v3 = self.transform(v3, modelMatrix)
            if self.active_texture:
                vt0 = model.texcoords[caritas[0][1] - 1]
                vt1 = model.texcoords[caritas[1][1] - 1]
                vt2 = model.texcoords[caritas[2][1] - 1]
                vt0 = (vt0[0], vt0[1])
                vt1 = (vt1[0], vt1[1])
                vt2 = (vt2[0], vt2[1])
                if vertCount > 3:
                    vt3 = model.texcoords[caritas[3][1] - 1]
                    vt3 = (vt3[0], vt3[1])
            else:
                #  vertices de texturas
                vt0 = (0, 0)
                vt1 = (0, 0)
                vt2 = (0, 0)
                vt3 = (0, 0)
                # vertices de normales
            vn0 = model.normals[caritas[0][2] - 1]
            vn1 = model.normals[caritas[1][2] - 1]
            vn2 = model.normals[caritas[2][2] - 1]
            vn0 = self.dirTransform(vn0, rotationMatrix)
            vn1 = self.dirTransform(vn1, rotationMatrix)
            vn2 = self.dirTransform(vn2, rotationMatrix)
            print(vn2)
            if vertCount > 3:
                vn3 = model.normals[caritas[3][2] - 1]
                vn3 = self.dirTransform(vn3, rotationMatrix)
            self.refillPolinizacion(v0, v1, v2, texcoords=(vt0, vt1, vt2), normals=(vn0, vn1, vn2))
            if vertCount > 3:
                self.refillPolinizacion(v0, v2, v3, texcoords=(vt0, vt2, vt3), normals=(vn0, vn2, vn3))
            if vertCount > 4   :#poligono 5
                self.refillPolinizacion(v0, v2, v3, texcoords=(vt0, vt2, vt3), normals=(vn0, vn2, vn3))
            """"""
            if vertCount >5: # poligono 6
                self.refillPolinizacion(v0, v2, v3, texcoords=(vt0, vt2, vt3), normals=(vn0, vn2, vn3))




    ###################### funcion que escribe el bmp  ##########################################
    def glFinish(self, filename):
        archivo = open(filename, 'wb')

        # header del archivo de  14 bytes
        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))
        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # header del Mitmap de 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))


        for x in range(self.height):
            for y in range(self.width):
                archivo.write(self.pixels[x][y])

        archivo.close()




        ##################################### Fill a polygon  lab 1 #############################

        """ El primer punto va a dibujar una linea  al siguiente punto que tiene 
         en su coordenada 
         
         flat Bottom   -  si el fondo es plano 
        flat top - si la superficie es plano
         """
        #  dibuja el poligono
    def pintaPol (self, points):
        cont =  len(points)
        for i in range(cont):
            v0 =points[i]
            v1= points[(i+1) % cont]
            self.glPrintLineaObj(v0[0], v0[1], v1[0], v1[1])




    # tenemos que definir que es un triangulo en nuestro multiverso
    """
        
    Leer pdfs de articulos adjuntos a la tarea 
       
    Literatura consultada  ear clipping    
    1. https://en.wikipedia.org/wiki/Polygon_triangulation#:~:text=Ear%20clipping%20method,-A%20polygon%20ear&text=An%20implementation%20that%20keeps%20separate,Hazel%20Everett%2C%20and%20Godfried%20Toussaint.
    
    2. http://cauchemarg.blogspot.com/2013/10/41-relleno-de-poligonos.html
    
    3. http://www.it.uu.se/edu/course/homepage/grafik1/ht05/Lectures/L02/LinePolygon/x_polyd.htm#:~:text=A%20single%20scan%20conversion%20is,by%20the%20polygon%20filling%20routine.&text=So%20the%20line%20algorithm%20travels,line%20for%20each%20Y%2Dcoordinate.
    
    
    implementacion del algoritmo para fillear con mas de cuatro lados  
    
    ALGORITMO SCAN CONVERSION ALGORITHM 
    dividir poligono en triangulos   > 5,6 y 7  lados no tiro error  
    
    
    
    
    """

    """ Generalized Barycentric Coordinates on Irregular Polygons  
        PDF adjuntado 
     
     A 
     B
     C 
     Lados 
     """


    # METODO BARICENTRICO leer pdf adjunto
    def refillPolinizacion(self, A , B, C , texcoords = (), normals = (), _color = None):
        print(" dame chance ")
        minX = round(min(A[0], B[0], C[0]))
        minY = round(min(A[1], B[1], C[1]))
        maxX = round(max(A[0], B[0], C[0]))
        maxY = round(max(A[1], B[1], C[1]))

        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if x >= self.width or x < 0 or y >= self.height or y < 0:
                    continue
                u, v, w = baricentricas(A, B, C, (x, y))

                    # si no son mayores a 0 ggplot
                if u >= 0 and v >= 0 and w >= 0:

                    z = A[2] * u + B[2] * v + C[2] * w


                    if z < self.zbuffer[y][x] and z <= 1 and z >= -1:
                        #b, g, r = self.colorPintar

                        if self.active_shader:
                            r, g, b = self.active_shader(
                             self,

                                baryCoords=(u, v, w),
                                texCoords=texcoords,
                                normals=normals,
                                color = _color or self.colorPintar)
                        else:
                                    # el que tiene o el que le mandan
                            b, g, r = _color or self.colorPintar

                       # print(str(r)+" "+str(g)+" "+str(b))
                        #print('pintando')
                        # guardar color punto para pintar cada punto del zbuffer
                        self.punto(x, y, color(r, g, b))
                        self.zbuffer[y][x] = z

#  funcion que me deja pintar una imagen obj como fondo

    def FondoBMP(self, pixels):
        self.pixels = pixels
        for y in range(self.height):
            linea = []
            for x in range(self.width):
                linea.append(pixels[y][x])
            self.pixels.append(linea)


    def glZBuffer(self, filename):
        archivo = open(filename, 'wb')

        # File header 14 bytes
        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))
        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # Image Header 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))

        # Minimo y el maximo
        minZ = float('inf')
        maxZ = -float('inf')
        for x in range(self.height):
            for y in range(self.width):
                if self.zbuffer[x][y] != float('inf'):
                    if self.zbuffer[x][y] < minZ:
                        minZ = self.zbuffer[x][y]

                    if self.zbuffer[x][y] > maxZ:
                        maxZ = self.zbuffer[x][y]

        for x in range(self.height):
            for y in range(self.width):
                depth = self.zbuffer[x][y]
                if depth == float('inf'):
                    depth = minZ
                depth = (depth - minZ) / (maxZ - minZ)
                archivo.write(color(depth, depth, depth))

        archivo.close()

    def rtRender(self):
        #pixel por pixel
        for y in range(self.height):
            for x in range(self.width):


                Px = 2 * ( (x+0.5) / self.width) - 1
                Py = 2 * ( (y+0.5) / self.height) - 1

                # fov
                t = tan( (self.fov * valorpi / 180) / 2 )
                r = t * self.width / self.height
                Px *= r
                Py *= t

                direction = [Px, Py, -1]
                direction = normal(direction)
                material = None
                intersect = None
                for obj in self.scene:
                    hit = obj.ray_intersect(self.camPosition,direction)
                    if hit  is not None:
                        if hit.distance < self.zbuffer[y][x]:
                            self.zbuffer[y][x] = hit.distance
                            material = obj.material
                            intersect = hit
                if material is not None:
                            light_dir = magnum(self.light.position, intersect.point)
                            light_dir = normal(light_dir)
                            intensity = self.light.intensity * max(0,productopunto(light_dir, intersect.normal))
                            r = intensity * self.light.color[2] / 255
                            g = intensity * self.light.color[1] / 255
                            b = intensity * self.light.color[0] / 255

                            r *= material.diffuse[2]
                            g *= material.diffuse[1]
                            b *= material.diffuse[0]

                            print(r)
                            print(g)


                            self.glVertex_coord(x,y, color(min(1,r),min(1,g),min(1,b)))




