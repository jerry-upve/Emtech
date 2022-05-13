#Ejercicio retador # 4
productos = [
    {"id": 1, "tipo": "Maíz grano", "CostoCaja": 285.55},
    {"id": 2, "tipo": "Pepino", "CostoCaja": 334.72},
    {"id": 3, "tipo": "Tomate verde", "CostoCaja": 129.00}
]

idProducto = int(input("ID del producto:"))
checkExistProductId = False
productoBuscado = {}

for producto in productos:
    if idProducto == producto["id"]:
        checkExistProductId = True
        productoBuscado = producto
        break


print("")

if checkExistProductId:
    numeroCajas = float(input("Número de cajas a vender:"))
    
    print("El producto es: " + productoBuscado["tipo"])
    print("El precio por caja es: " + str(productoBuscado["CostoCaja"]))
    print("El total a pagar es: " + str(numeroCajas * productoBuscado["CostoCaja"]))
else:
    print("El pruducto con el id " + str(idProducto) + " no existe")
