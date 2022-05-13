productos = [
    {"id": 1, "tipo": "Maíz grano", "CostoCaja": 285.55},
    {"id": 2, "tipo": "Pepino", "CostoCaja": 334.72},
    {"id": 3, "tipo": "Tomate verde", "CostoCaja": 129.00}
]

venta_productos = [[2, 122], [1, 89], [1, 22], [3, 48], [1, 75],[3, 322],[2, 95],[1, 148],[1, 83],[3, 100]]

idProducto = int(input("ID del producto:"))
checkExistProductId = False
productoBuscado = {}
totalCajasVendidas = 0

for producto in productos:
    if idProducto == producto["id"]:
        checkExistProductId = True
        productoBuscado = producto
        for venta in venta_productos:
            if idProducto == venta[0]:
                totalCajasVendidas += venta[1]
        break

if checkExistProductId:
    numeroCajas = int(input("Número de cajas a vender:"))
    print("")
    print("El producto es: " + productoBuscado["tipo"])
    print("El precio por caja es: $" + str(productoBuscado["CostoCaja"]))

    totalPagar = 0
    checkCostoEnvio = 0
    if numeroCajas > 100:
        totalPagar = numeroCajas * productoBuscado["CostoCaja"]
        print("costo de envío: $0")
    else: 
        totalPagar = numeroCajas * productoBuscado["CostoCaja"] + 1500
        print("costo de envío: $1500.00")

    if totalCajasVendidas < 1500:
        descuento = (totalPagar * 20) / 100
        print("Aplica descuento del 20%: Si")
        print("El total a pagar es: $" + str(totalPagar - descuento))
    else:
        print("Aplica descuento del 20%: No")
        print("El total a pagar es: $" + str(totalPagar))
else:
    print("El pruducto con el id " + str(idProducto) + " no existe")
