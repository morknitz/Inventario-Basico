def mostrar_menu():
    inventario = [] 
    opcion = 0
    while opcion != 6:
        print("\n---Inventario Basico---")
        print("1. Agregar producto")
        print("2. Mostrar producto")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = int(input("Ingresa una opcion: "))

        if opcion == 1:
            agregar(inventario)
        elif opcion == 2:
            mostrar(inventario)
        elif opcion == 3:
            buscar(inventario)
        elif opcion == 4:
            modificar(inventario)
        elif opcion == 5:
            eliminar(inventario)
        elif opcion == 6:
            print("...Ha salido del inventario")
        else:      
            print("---La opcion no es valida")

def agregar(inventario):  
            cantidad = int(input("cuantos productos quiere agregar: "))
            for i in range(cantidad):
                nombre = input("Ingrese el nombre del producto: ")
                if nombre == "":    
                    print("No se permiten nombres vacíos")
                else:
                    precio = float(input("Ingrese el precio: $"))
                    cantidad = int(input("Ingrese la cantidad: C/"))
                    producto = {     
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad,
                    }
                    inventario.append(producto)  
                    print("---Producto(s) agregado(s)")

def mostrar(inventario):
        if inventario == []:
            print("---No hay inventario registrado")
        else:
            print("\n---producto(s) registrado(s)")
            contador = 1
            for producto in inventario:
                print(
                    contador,
                    "-",
                    producto["nombre"],
                    "-$",
                    producto["precio"],
                    "-C/",
                    producto["cantidad"],
                )
                contador += 1

def buscar(inventario):
        buscar = input("Nombre del producto: ") 
        encontrado = False
        for producto in inventario:
            if producto["nombre"].lower() == buscar.lower():  
                encontrado = True
                print("\n---Producto encontrado")
                print("Nombre:", producto["nombre"])
                print("Precio: $", producto["precio"])
                print("Cantidad: C/", producto["cantidad"])
                break
        if not encontrado:  
            print("---No existe el producto")
    
def modificar(inventario):  
        buscar = input("producto a modificar:")
        encontrado = False
        for producto in inventario:
            if producto["nombre"].lower() == buscar.lower():
                producto["precio"] = float(input("Nuevo precio: $"))
                producto["cantidad"] = int(input("Nueva cantidad: C/"))
                print("---Producto actualizado")
                encontrado = True
                break
        if not encontrado:  
            print("---No existe el producto")

def eliminar(inventario):  
        eliminar = input("producto a eliminar: ")
        encontrado = False
        for producto in inventario:
            if producto["nombre"].lower() == eliminar.lower():
                inventario.remove(producto)    
                print("---Producto eliminado")
                encontrado = True
                break
        if not encontrado: 
            print("---No existe el producto")

mostrar_menu()