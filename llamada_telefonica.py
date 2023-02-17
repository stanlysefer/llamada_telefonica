#Programa para calcular el tiempo de duracion de una llamada telefonica y de terminar la cantidad a pagar, deacuerdo con lo siguiente: 

# Toda llamada que dure 3 minutos o menos tiene un costo de $300
# Cada minuto adicional cuesta $50 

print("--------------------------------")
print("------ INGRESE UN NUMERO -------")
print("--------------------------------")

#input
minutos = int(input("INGRESE LOS MINUTOS DE LA LLAMADA: "))

#processing

if minutos <= 3:
    costo = 300

else:
    costo = 300 + (minutos - 3) * 50


# output
print("---------------------------------")
print("----------- RESULTADO -----------")
print("---------------------------------")

print("el costo de la llamada es: ", costo)