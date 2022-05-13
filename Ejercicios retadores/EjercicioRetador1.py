# Damos demograficos y poblacionales  del estado de sinaloa.
datosSinaloa = {
    "superficieKm": 57365,
    "localizacion": "noroeste",
    "climas": ["cálido","subhúmedo","seco","semiseco"],
    "temperaturaAnualGrados": 25.45,  #grados centígrados
    "precipitacionAnualmm": 790.1, #mm
    "poblacionMujeres": 1532128,
    "poblacionHombres": 1494815,
    "municipiosMasPoblados": [
        {"nombre": "Culiacán", "porcetanjeHabitantes": 33.15},
        {"nombre": "Mazatlán", "porcetanjeHabitantes": 16.57}
    ]
}

sinaloaPoblacionTotal = datosSinaloa["poblacionHombres"] + datosSinaloa["poblacionMujeres"]

print("-----------------------------------------------------------")
print("Informacion demografica y poblacinal del estado de Sinaloa")
print("")
print("Superficie total: " + str(datosSinaloa["superficieKm"]) + "km")
print("Localización: " + datosSinaloa["localizacion"])
print("Temperatuta anual promedio: " + str(datosSinaloa["temperaturaAnualGrados"]) + " °C")
print("Precipitación anual promedio: " + str(datosSinaloa["precipitacionAnualmm"]) + " mm")
print("Tipos de clima:")

for clima in datosSinaloa["climas"]:
    print(" -" + clima)

print("")
print("Población total: " + str(sinaloaPoblacionTotal))
print("Población Mujeres: " + str(datosSinaloa["poblacionMujeres"]))
print("Población Hombres: " + str(datosSinaloa["poblacionHombres"]))
print("Municipios mas poblados: ")

for municipio in datosSinaloa["municipiosMasPoblados"]:
    print(" " + municipio["nombre"] + " con el " + str(municipio["porcetanjeHabitantes"]) + "% de la población")



