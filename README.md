<h1 align="center">	Recursividad</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Recursividad)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea hemos resuelto una serie de ejercicios aplicando el método de la recursividad.

***

## Índice

1. [Ejercicio 5](#id1)
2. [Ejercicio 6](#id2)
3. [Ejercicio 7](#id3)

***


## Ejercico 5:<a name="id1"></a>


```

tabla = [1,2,3,4,5,6,7,8]
n = int(input('Introduzca el valor que desea encontrar:'))
i = 0
j = len(tabla)
m = (i+j)/2

class tablas:
  def  __init__(self,tabla,n,i,j):
    self.i= i
    self.j= j
    self.n= n
    
  def busqueda_numero (self):
    
    if self.i > self.j:
      return'No hay ningún valor en la posición seleccionada'
      
    else:
      self.m = m
      if tabla[self.m] == n:
        return self.m
      elif tabla[self.m] > n:
        print (busqueda_numero(self))
        return busqueda_numero (self,self.m -1)
      else:
        return busqueda_numero (self, self.m + 1)
        
  return busqueda_numero
```
***


## Ejercicio 6:<a name="id2"></a>


***

## Ejercicio 7:<a name="id3"></a>


***
