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
        
  
  resultado = tablas(tabla,n,j,i)
  print(resultado.busqueda_numero())
```
***


## Ejercicio 6:<a name="id2"></a>

```
palabra = str(input('Introduzca una palabra:'))

class verificacion:
  def __init__(self,palabra):
    self.palabra = palabra
  def palabra_palindroma (self):
    if str(self.palabra) == str(self.palabra)[::-1]:
      print ('La palabra es palindroma')
    else:
      print('La palabra no es palindroma')
  
resultado = verificacion(palabra)
print(resultado.palabra_palindroma)

p= palabra
x = ''
remplazadores = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
class convertidor:
  def __inti__(self,p):
    self.p = p
    self.x = x
    self.remplazadores= remplazadores
  def convertir_a_mayúcula (self):
    if p.islower(): #Esto lo usamos para comprobar si esta en minúscula
      return p.upper()
    else:
      print (p)

  def detector_caracteres_no_alfanuméricos(self):
    self.x = ''.join(ch for ch in p if ch.isalnum()) #Podemos utilizar el método isalnum() para comprobar si un carácter o cadena dada es alfanumérico o no. Podemos comparar cada carácter individualmente de una cadena, y si es alfanumérico, lo combinamos usando la función join().


    print(self.x)

  def eliminador_acentos(self):
    for a, b in remplazadores:
        p = p.replace(a, b).replace(a.upper(), b.upper())
    return p

resultado2 = convertidor(x, remplazadores, p)
print(resultado2.convertir_a_mayuscula())
print(resultado2.detector_caracteres_no_alfanuméricos())
print(resultado2.eliminador_acentos())
```


***

## Ejercicio 7:<a name="id3"></a>

```
  def reorganizar_colores(self):
    if len(self.bandera) > 0:
      color = self.bandera.pop(0)

    if color == "R":
      self.rojo.append(color)
      return self.bandera
    if color == "A":
      self.azul.append(color)
      return self.bandera
    if color == "V":
      self.verde.append(color)
      return self.bandera
    else:
        resultado_bandera=rojo+verde+azul
        print('La bandera ordenada es la siguiente: {resultado_bandera}')

resultado=organizacion(bandera,rojo,verde,azul)
print(resultado.reorganizar_colores)
    
    
```


***
