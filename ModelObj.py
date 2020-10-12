"""

Universidad del Valle de Guatemala
Graficas por computadora
Obj
Jorge Suchite Carnet 15293
07/07/2020
Lab 1  Fill polygon


"""

import struct
from LibreriaGL import *
class ModelObJ(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.modobj()



#### muchos objs vienen con diferentes signos de puntuacion para separar varias cosas
### en este caso se arreglaron los que a mi me aparecieron
    def modobj(self):
        for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    continue

                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                    # normales
                elif prefix == 'vn':
                    self.normals.append(list(map(float,value.split(' '))))
                    #coordens
                elif prefix == 'vt':
                    self.texcoords.append(list(map(float,value.split(' '))))
                    #caras
                elif prefix == 'f':
                    caras = value.split(' ')
                    lista = []
                    for cara in caras:
                        if cara != '':
                            c = cara.split('/')
                            vector = []
                            for x in c:
                                try:
                                    vector.append(int(x))
                                except:
                                    print(str(x))

                            lista.append(vector)
                    self.faces.append(lista)
        print("Si se pudo cargar")


        #### leer obj



class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, 'rb')
        image.seek(10)

        # print headerSize
        headerSize = struct.unpack('=l', image.read(4))[0]

        image.seek(14 + 4)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]

        # que se vaya a leer al header y no a la posicion 54
        image.seek(headerSize)

        self.pixels = []

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):

                # valor de 0 a 1 / 255
                b = ord(image.read(1)) / 255
                g = ord(image.read(1)) / 255
                r = ord(image.read(1)) / 255
                self.pixels[y].append(color(r, g, b))

        image.close()

    def getColor(self, textxcolor, textcolory):
        if textxcolor >= 0 and textxcolor <= 1 and textcolory >= 0 and textcolory <= 1:
            x = int(textxcolor * self.width)
            y = int(textcolory * self.height)

            return self.pixels[y][x]
        else:
            return color(0, 0, 0)


