puntajes = []

puntajes.append(1000)
puntajes.append(920)
puntajes.append(830)
puntajes.append(750)
puntajes.append(670)

puntajes.remove(920)
puntajes.remove(830)
puntajes.remove(750)

contador = 0

cantidadPuntajes = input("Por favor indique la cantidad de puntajes a ingresar")

while not cantidadPuntajes.isdigit():
  cantidadPuntajes = input("Por favor indique la cantidad de puntajes a ingresar")

while contador < int(cantidadPuntajes):
  contador += 1
  puntaje = input("Ingrese el puntaje: ")
  puntajes.append(int(puntaje))
print("Los mejores puntajes son: ")
print(puntajes)