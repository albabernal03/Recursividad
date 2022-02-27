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
class convertidor:
  def __inti__(self,p):
    self.p = p
  def convertir_a_mayúcula (self):
    if p.islower(): #Esto lo usamos para comprobar si esta en minúscula
      return p.upper()
    else:
      print (p)
  

 