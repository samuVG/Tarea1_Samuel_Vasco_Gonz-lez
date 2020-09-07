#!/usr/bin/env python
# coding: utf-8

# In[103]:


def Factorial(n):
    if n==0:  #se define el factorial de 0 igual a 1 
        return 1
    if n<0 or int(n**2)!=n**2:
        print("no es entero positivo")
    else:
        fac=1  #se inicializa el contador
        for i in range (2,n+1): #se crea un for para iterar la multiplicación recursiva
            fac=fac*i #se guarda el resultado de la multiplicación iterativamente de forma recursiva
        return fac #se retorna el factorial de n
    


# In[104]:


def Binomial(n,k): #se define la función Binomial(n,k)
    bin=Factorial(n)/(Factorial(k)*Factorial(n-k)) #se invoca la función Factorial(n) y se escribe la ecuación de coeficientes Binomiales explícitamente
    return bin #se retorna el coeficiente Binomial de (n,k)


# In[105]:


def Pascal(n): # se define la función Pascal(n), con n el número de filas del triángulo de Pascal
    import os #se importa la librería para manipulación de archivos
    file=open("Pascal-"+str(n)+".txt","w") # se crea el archivo Pascal-n.txt 
    
    for j in range(0,n+1): #primer ciclo for para crear las filas del triángulo de Pascal y definir hasta dónde irán las binomiales
        a=[] #se crea una lista donde se guardarán los elementos de cada fila del triángulo
        for i in range (0,j+1): #segundo ciclo for para hallar los elementos de cada fila del triángulo a partir de la binomial
            b=int(Binomial(j,i)) #se halla elemento a elemento de la fila del triángulo y se convierte en número entero
            a.append(b) #se guarda el resultado de la binomial en la lista 
        file.write("n=%s  "%i) #se escribe el número n de cada fila del triángulo en el archivo .txt
        a=str(a) #se convierte la lista en string para quitar los corchetes y las comas
        a=a.replace("[","").replace("]","").replace(",","    ")
        
        file.write(((2*(n+9-j)-j-4*int(j/10)))*" "+a+os.linesep)
    
    file.close() #se cierra el archivo .txt
    return #se cierra la función Pascal(n)


# In[106]:


Pascal(10)


# In[ ]:




