#Ejercicio retador # 3
pesoCostalCemento = 40 #kg
pesoCostalYeso = 30 #kg
camionLimiteCapacidad = 3254 #kg

costalesCemento = int(input("Número de costales de cemento:"))
costalesYeso = int(input("Número de costales de yeso:"))

pesoTotal = (costalesCemento * pesoCostalCemento) + (costalesYeso * pesoCostalYeso)

print("")
print("El peso total es: " + str(pesoTotal) + "kg")

if pesoTotal <= camionLimiteCapacidad:
    if pesoTotal >= camionLimiteCapacidad / 2:
        print("¿Se puede realizar el envío?: Si")
    else:
        print("¿Se puede realizar el envío?: No")
        print("El peso no cumple con el minimo requerido para le envio")
else:
    print("¿Se puede realizar el envío?: No")
    print("El peso supera el limite del camion")
