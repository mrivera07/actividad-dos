#coversacion de cadena a enteros

cadena_a_entero=int("2024")
print(cadena_a_entero)

#conversacion de cadena a flotante
cadena_a_flotante =  float("18.0")
print(cadena_a_flotante)

#conversacion de numero a cadena
numero_a_cadena =str(4568)
print(numero_a_cadena)

#multilineas de cadena utilizando triple comillas
texto_multilineas = """este es un ejemplo de python que imprime con 3n comillas """
print(texto_multilineas)

# uso de la funcion len () para obtner la longitud de una cadena
mi_cadena ="Hola Mundo aqui estamos aprendiendo python 2024"
longitud=len(mi_cadena)
print ("longitud de la cadena :",longitud)

#obtener los primeros n caracteres de una cadena
n=10
cadena ="Hola mundo 2024"
primeros_n = cadena [:n]
print ("primeros",n,"caracteres:",primeros_n)

#obtener caracteres en mediod e cadena
inicio=5
fin = 10
medio =cadena[inicio:fin]
print ("caracteres de en medio :",medio)

#obtener los ultimos caracteres de una cadena
n=5
ultimos_n =cadena [-n:]
print("ultimos ",n,"caracteres:", ultimos_n)

#funcion upper
#convertir una cadena  a mayusculas
cadena="Yina marcela calvacha rivera"
cadena_mayus=cadena.upper()
print("cadena en ,asyusculas :", cadena_mayus)

#convertir cadena a minuculas
cadena ="YINA MARCELA CALVACHE RIVERA"
cadena_minus =cadena.lower()
print("cadena en minusculas :",cadena_minus)

#uso de las cadenas multilinea con comillas triples
texto_multilineas =""" esra es una cadena
que ocupa varias lineas
-----Hola mundo-----
------python 2024------
-----Marcela------"""
print(texto_multilineas)

#eliminacion de espacios en blanco al principio y al final de una cadena
cadena_con_espacios = "Hola Mundo estamos aprendiendo python"
cadena_sin_espacios=cadena_con_espacios.strip()
print("aqui vemos la cadena sin espacios:",cadena_sin_espacios)

#reemplazar un texto especifico por otro
cadena_original="Marcela le gusta salir a conocer lugares "
cadena_reemplazada =cadena_original.remplace("marcela","le gusta")
print("cadena remplazada:",cadena_reemplazada)

#dividir una cadena en una listad e palabras
cadena="Hola mundo estamos aprendiendo python"
lista_palabras =cadena.split()
print ("lista de palabras ", lista_palabras)

#uso de f strings para formatear cadenas
nombre="Yina Marcela calvache rivera"
edad=20
mensaje=f"Hola. mi nombre {nombre} y tengo {edad}años"
print(mensaje) #salida: ´hola mi nombre es ana y tengo 25 años .