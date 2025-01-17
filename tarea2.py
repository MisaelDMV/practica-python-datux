ventas=[
    {
        "fecha":"12-01-2023",    
        "producto:":"Producto_A",                                                                                                                        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },

    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },

    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },

    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

def AñadirProducto():
    fecha = input("Ingrese la fecha (ejemplo: 12-12-2021):")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese su cantidad de ventas: "))
    precio = float(input("Ingrese el precio del producto: "))
    promocion = input("¿Este producto cuenta con una promoción? (sí/no): ").lower() == "sí"

    nuevoProducto = {
        "fecha": fecha,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "promocion": promocion
    }

    ventas.append(nuevoProducto)
    print("producto agregado")

def sumaTotal():
        sTotal = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
        print(f"El total de las ventas sería: {sTotal:.2f}")

def PromDeVentas():
        if ventas:
            total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
            promedio = total / len(ventas)
            print(f"El promedio de las ventas es: {promedio:.2f}")
        else:
            print("No hay ventas en el sistema")

def ProductoMasVendido():
          VentasPorProducto = {}
          for venta in ventas:
             producto = venta["producto"]
             cantidad = venta["cantidad"]
          if producto in VentasPorProducto:
            VentasPorProducto[producto] += cantidad
          else:
            VentasPorProducto[producto] = cantidad

            producto_max = max(VentasPorProducto, key=VentasPorProducto.get)
            cantidad_max = VentasPorProducto[producto_max]
    
            print(f"El producto con más unidades vendidas sería: {producto_max} ({cantidad_max} unidades)")

def ListadoProductos():
    productos = {venta["producto"] for venta in ventas}
    print("Lista de productos:")
    for producto in productos:
        print(f"- {producto}")

def menu():
    print("-------BIENVENIDO AL MENÚ DE OPCIONES-------")
    print("1. Mostrar el listado de ventas")
    print("2. Añadir un producto")
    print("3. Calcular la suma total de las ventas")
    print("4. Calcular el promedio de ventas")
    print("5. Mostar el producto mas unidades vendidas")
    print("6. Mostrar el listado de productos")
    eleccion = int(input("Elija una opción:"))

    if eleccion == 1:
         print(ventas)

    elif eleccion == 2:
         AñadirProducto()

    elif eleccion == 3:
        sumaTotal()

    elif eleccion == 4:
        PromDeVentas()

    elif eleccion == 5:
        ProductoMasVendido()

    elif eleccion == 6:
        ListadoProductos()  

    else:
        print("Esa no es una opción")   
menu()





