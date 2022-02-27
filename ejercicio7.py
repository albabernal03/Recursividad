#R= ROJO
#V=VERDE
#A=AZUL
bandera = ["R","A","A","R","V","A","A","R","A","R","R","V","R","R","A","V","V"] #El orden ya viene dado por el ejercicio
rojo = []
verde=[]
azul=[]

class organizacion:
  def __init__(self,bandera,rojo,verde,azul):
    self.bandera=bandera
    self.rojo=rojo
    self.verde=verde
    self.azul=azul
  def reorganizar(self):