#Ejercicio retador numero 2
municipios = []
totalHabitantes = 0
habitantesPromedio = 0

i = 0
while i < 3:
    nombreMunicipio = input("Ingresa el nombre del municipio:")
    numeroHabitantes = input("Ingresa el numero de habitantes del municipio:")
    municipios.append({
        "nombre": nombreMunicipio,
        "habitantes": numeroHabitantes
    })
    i += 1

print("")
print("Municipios:")

for municipio in municipios:
    print(" -" + municipio["nombre"] + ": " + municipio["habitantes"] + " habitantes")
    totalHabitantes += int(municipio["habitantes"])

print("")
print("El total de habitantes es: " + str(totalHabitantes))
print("El promedio de habitantes es: " + str(totalHabitantes / len(municipios)))
