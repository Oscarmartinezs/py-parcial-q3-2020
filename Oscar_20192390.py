import math
from unittest import result

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(num1, num2):
    return num1 * num2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    resultado = 0
    total = 0
    while resultado < 1000:
        if (resultado % 3 == 0) and (resultado % 5 == 0):
            total = total + resultado

        result = resultado + 1

    return total


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
def definicionCono(altura, radio):
    altura = 11
    radio = 5
    #definir el cono
    definicion = dict{'generatriz ': math.sqrt((pow(altura,2)) + (pow(radio,2))), 
                    'area '_:  (math.pi)*(radio)*(radio) + ((math.sqrt((pow(altura,2)))+(pow(radio,2)))),
                    'volumen ': (1/3)*(math.pi)(pow(radio,2)(altura)
    }
        result = definicion
    return result


def obtenerGeneratriz(altura,radio):
    #obtener la generatriz
    result = math.sqrt(pow(altura,2) + pow(radio,2))
    return result


def obtenerArea(altura, radio):
    #obtener el area
    area= (math.pi)*(radio)*(radio+(math.sqrt((pow(altura,2)) + (pow(radio,2)))))
    result = area
    return result


def obtenerVolumen(altura, radio):
    #obtener el volumen
    volumen = (1/3)*(math.pi)*(pow(radio,2))*(altura)
    result = volumen
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
    def definicionCono(self, altura, radio):
    self.altura = 11
    self.radio = 5
    self.definicion = dict{'generatriz ': math.sqrt((pow(self.altura,2)) + (pow(self.radio,2))), 
                    'area':  (math.pi)*(self.radio)*((self.radio) + ((math.sqrt((pow(self.altura,2)))+(pow(self.radio,2))))),
                    'volumen ': (1/3)*(math.pi)(pow(self.radio,2)(self.altura)
                    }
    return self.definicion


def obtenerGeneratriz(self, altura,radio):
    self.result = math.sqrt(pow(self.altura,2) + pow(self.radio,2))
    return self.result


def obtenerArea(self, altura,radio):
    self.area= (math.pi)*(self.radio)*(self.radio+(math.sqrt((pow(self.altura,2)) + (pow(self.radio,2)))))
    return self.area


def obtenerVolumen(self, altura,radio):
    self.volumen = (1/3)*(math.pi)*(pow(self.radio,2))*(self.altura)
    return self.volumen



"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico:
    def registrar(self):
        return 0

    def totalCostoSanSalvador(self):
        return 0

    def totalCostoConDescuento(self):
        return 0


class Paciente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url

ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
