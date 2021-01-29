# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 00:58:22 2020

@author: jalil garcia jeronimo
"""
print ("introdusca un numero")#se solicita un dato desde el teclado
num=int(input())#se almacena el dato introducido desde el teclado

def factorial(num):#Funcion recursiva
   if num == 0 or num == 1:#condicion o caso base
      return 1
   else:
      return num * factorial(num - 1)#se llama la funcion asi mismo,creando un buclea hasta llegar a igualar la condicion o funcion  
print (factorial(num)) #se imprime el valor obtenido del factorial