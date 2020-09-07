#!/usr/bin/env python
# coding: utf-8

# In[3]:


import funciones #se invocan las funciones creadas en el módulo funciones

#Ejercicio 4: se lanza una moneda n veces
# a). la probabilidad de que si se hace este experimento 100 veces, el resultado sean 10 veces cara.

def Probabilidad(n,k):  #funcion que calcula la probabilidad de que cuando se lanza una moneda n veces
    prob=funciones.Binomial(n,k)/2**n  # y resulte un numero k de veces cara (sello)
    return prob

print("Punto a).")
print("La probabilidad de lanzar 100 veces una moneda y caiga 10 veces cara es: ",Probabilidad(100,10))
print("La probabilidad de que suceda es del orden de 10^(-15)% \n")

suma=0
for i in range(31,101): # se suman las probabilidades desde 31 hasta 100
    suma=suma+Probabilidad(100,i)

print("Punto b).")
print("La probabilidad de lanzar 100 veces una moneda y caiga más de 30 veces cara es: ",suma)
print("La probabilidad de que suceda es del orden de 99.996%")


# In[ ]:




