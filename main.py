import presentation


def iniciar():
    while True:
        presentation.mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            presentation.ejecutar_opcion(opcion)
            break

        presentation.ejecutar_opcion(opcion)


if __name__ == "__main__":
    iniciar()