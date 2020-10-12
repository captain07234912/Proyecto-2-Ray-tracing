
from LibreriaGL import *
import numpy as np

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/09/2020
DR1 :  Spheres and Materials

"""

White = (1,1,1)

class Light(object):
    def __init__(self, position = (0,0,0), colorluz = White, intensity = 1):
       self.position = position
       self.color = colorluz
       self.intensity = intensity


class Material (object):
    def __init__(self, diffuse = White):

        self.diffuse = diffuse

        return

class Intersect (object):
    def __init__(self,distance, point, normal):
        self.distance = distance
        self.normal = normal
        self.point = point
class Sphere(object):
    def __init__(self, center, radius, material ):
        self.center = center
        self.radius = radius
        self.material = material


    def ray_intersect(self, orig, dir ):
        L = magnum(self.center, orig)
        tca = productopunto(L, dir)
        l = magnum2(L)  # magnitud de L
        d = (l ** 2 - tca ** 2) ** 0.5
        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0:  # t0 ahora es t1
            return None

        dir =[ dir[0]*t0,
             dir[1]*t0,
             dir[2]*t0]

        point = Suma(orig,dir)
        normal1 = magnum(point,self.center)
        normal1 = normal(normal1)


        return  Intersect(distance= t0, point= point, normal = normal1)