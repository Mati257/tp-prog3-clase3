import business


def mostrar_menu():
    print("\n==============================")
    print("       CONTROL DE STOCK")
    print("==============================")
    print("1. Añadir producto")
    print("2. Añadir cantidad de stock")
    print("3. Añadir una unidad")
    print("4. Quitar una unidad")
    print("5. Consultar stock")
    print("6. Salir")
    print("==============================")


def ejecutar_opcion(opcion):
    if opcion == "1":
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")

        resultado, mensaje = business.agregar_producto(codigo, nombre)

        print(mensaje)

    elif opcion == "2":
        codigo = input("Ingrese el código del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))

        resultado, mensaje = business.agregar_stock(codigo, cantidad)

        print(mensaje)

    elif opcion == "3":
        codigo = input("Ingrese el código del producto: ")

        resultado, mensaje = business.agregar_unidad(codigo)

        print(mensaje)

    elif opcion == "4":
        codigo = input("Ingrese el código del producto: ")

        resultado, mensaje = business.quitar_unidad(codigo)

        print(mensaje)

    elif opcion == "5":
        codigo = input("Ingrese el código del producto: ")

        stock = business.consultar_stock(codigo)

        if stock is None:
            print("El producto no existe.")
        else:
            print(f"Stock actual: {stock}")

    elif opcion == "6":
        print("Programa finalizado.")

    else:
        print("Opción inválida.")