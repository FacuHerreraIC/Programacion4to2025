
#Importar el módulo datetime.
import datetime
#Crear una variable llamada ahora y guardar la fecha actual utilizando la 
#función datetime.datetime.now(). Luego, realizar un print() de la variable ahora.
ahora = datetime.datetime.now()
print(ahora)
#Crear una variable llamada fecha y guardar la fecha de tu cumpleaños 
#utilizando la función datetime.datetime(AÑO, MES, DÍA). 
#Luego, realizar un print() de la variable fecha.
fecha = datetime.datetime(2000,1,1)
print(fecha)
#Crear una variable llamada diferencia, que guarde el resultado de 
#restar las variables ahora y fecha. 
#Luego, realizar un print() de la variable diferencia.
diferencia = ahora - fecha
print(diferencia)

#Crear una variable llamada diferenciaEnDias y guardar solo los días 
#de la resta anterior usando diferencia.days. 
#Luego, realizar un print() de la variable diferenciaEnDias.
diferenciaEnDias = diferencia.days
print(diferenciaEnDias)
#Crear una variable llamada anios, que guarde el resultado de 
# dividir la variable diferenciaEnDias entre 365. Luego, 
# realizar un print() de la variable anios.
anios = diferenciaEnDias / 365
print(anios)

#Realizar un print() con el texto → "Tengo ____ años" (usando concatenación).
#Atención: Dentro de la concatenación deberás utilizar el método int() 
#sobre la variable anios para eliminar los decimales y luego convertirlo 
#a cadena de texto con el método str() para poder concatenar correctamente.
print("Tengo "+str(int(anios))+" años")