import struct

# struct library es para estructuras binarias de datos

"""Universidad del Valle de Guatemala
    Graficas por computadora
    Clase que tiene funciones para todo el curso
    Jorge Suchite Carnet 15293
    07/07/2020

    Fill a polygon
"""


# Creador del BMP
# Creador del punto
# creador de la linea
# creador de obj
# creador de poligono filleado


# 1 byte  reservado en memoria
def char(c):
    return struct.pack('=c', c.encode('ascii'))


# 2  reservado bytes en memoria

def word(w):
    return struct.pack('=h', w)


# 4  reservado bytes en memoria

def dword(d):
    return struct.pack('=l', d)


# colores que son aceptados en bytes pero ahora seran con coordenadas ingresadas de 0 a 1


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

########################### Lista de colores para probar
Fondo = color(0.7,0.6,0.8)
Blanco = color(1,1,1)
CYANS = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)

valorpi = 3.14159


###################### baricentrico



"""
https://es.wikipedia.org/wiki/Coordenadas_baric%C3%A9ntricas

u = A
v = B
w = C
  
"""


valorpi = 3.14159
def baricentricas(A, B, C, P):

    try:
        u = ( ((B[1] - C[1])*(P[0] - C[0]) + (C[0] - B[0])*(P[1] - C[1]) ) /
              ((B[1] - C[1])*(A[0]- C[0]) + (C[0] - B[0])*(A[1] - C[1])) )

        v = ( ((C[1] - A[1])*(P[0] - C[0]) + (A[0] - C[0])*(P[1] - C[1]) ) /
              ((B[1] - C[1])*(A[0] - C[0]) + (C[0] - B[0])*(A[1] - C[1])) )

        w = 1 - u - v
    except:
        return -1, -1, -1

    return u, v, w



################## multiplicacion de una matriz yaw pitch roll



def productomatriz(filas , columnas):


    #4x4
    matriz = [ [0,0,0,0], [0,0,0,0],  [0,0,0,0],  [0,0,0,0]]
    for i in range(len(filas)):
        for j in range(len(columnas[0])):
            for k in range(len(columnas)):
                matriz[i][j] += filas[i][k] * columnas[k][j]
    return matriz
    """
    # matriz resultante
    matriz = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    for i in range(len(fillas)):  # Filas
        for j in range(len(columnas[0])):  # Columnas
            for k in range(len(columnas)):
                resMatrix[i][j] += filas[i][k] * columnas[k][j]

    return matriz
    """




a = [[1,2,3,4],[1,2,3,4],[0,0,0,0],[1,1,1,1]]
b = [[1,1,1,1]]

zape = productomatriz(a, b )
#print(zape)

def radianes (radianes2):
    return radianes2 * (valorpi/180)


def productopunto(v1, v2):
    return sum([(v1[i] * v2[i]) for i in range(3)])


# producto cruz para las normales



def productocruz(v1,v2):
    print(v2)
    matrizresultante  = [v1[1] * v2[2] - v1[2] * v2[1],
    v1[2] * v2[0] - v1[0] * v2[2],
    v1[0] * v2[1] - v1[1] * v2[0]]


    return matrizresultante



    """
 Parte de la camara
 inversa
 determinante 
 transpuesta
 
 stack overflow 
    """
def Transpuesta(m):
    return list(map(list,zip(*m)))

def MatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def Determinante(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    deter = 0
    for c in range(len(m)):
        deter += ((-1) ** c) * m[0][c] * Determinante(MatrixMinor(m, 0, c))
    return deter

def  Inversa(m):
    determinant = Determinante(m)

    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]


    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = MatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * Determinante(minor))
        cofactors.append(cofactorRow)
    cofactors = Transpuesta(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def normal(norm):

    largo = (norm[0] ** 2 + norm[1] ** 2 + norm[2] ** 2) ** (1 / 2)
    norm[0] =  (norm[0] / largo)
    norm[1] = (norm[1] / largo)
    norm[2] =  (norm[2] / largo)
    return norm

    return norm

def  magnum(v0, v1):


    resultado = [v0[0] - v1[0], v0[1] - v1[1], v0[2] - v1[2]]
    return resultado


def magnum2(vector):
    try:
        # largo del vector
        largo = (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) **(1/2)
    except ZeroDivisionError:

        return 0
    return largo



def Suma(list1, list2):
    suma = []
    if (len(list2) >= len(list1)):
        for i in range(len(list1)):

            suma.append(list1[i] + list2[i])
    return suma
