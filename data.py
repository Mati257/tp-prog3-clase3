productos = {}


def agregar_producto(codigo, nombre):
    if codigo in productos:
        return False

    productos[codigo] = {
        "nombre": nombre,
        "stock": 0
    }

    return True


def obtener_producto(codigo):
    return productos.get(codigo)