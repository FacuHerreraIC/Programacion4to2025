# Lista de puntajes inicial 
puntajes = [850, 920, 670, 750, 830, 1000]
minimo = min(puntajes)
print(minimo)
maximo = max(puntajes)
print(maximo)
promedio = sum(puntajes) / len(puntajes)
print(promedio)
puntajes.reverse()
print(puntajes)
puntajes.sort()
print("El TOP SCORE final es: ")
print(puntajes)

contador = 0
while contador < len(puntajes):
    print(puntajes[contador])
    contador+=1

for puntaje in puntajes:
    print(puntaje)