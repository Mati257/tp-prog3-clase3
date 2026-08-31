import data


def agregar_producto(codigo, nombre):
    producto = data.obtener_producto(codigo)

    if producto is not None:
        return False, "El producto ya existe."

    data.agregar_producto(codigo, nombre)

    return True, "Producto agregado correctamente."


def agregar_stock(codigo, cantidad):
    producto = data.obtener_producto(codigo)

    if producto is None:
        return False, "El producto no existe."

    if cantidad <= 0:
        return False, "La cantidad debe ser mayor a cero."

    producto["stock"] += cantidad

    return True, "Stock agregado correctamente."


def agregar_unidad(codigo):
    return agregar_stock(codigo, 1)


def quitar_unidad(codigo):
    producto = data.obtener_producto(codigo)

    if producto is None:
        return False, "El producto no existe."

    if producto["stock"] <= 0:
        return False, "No hay stock disponible."

    producto["stock"] -= 1

    return True, "Unidad quitada correctamente."


def consultar_stock(codigo):
    producto = data.obtener_producto(codigo)

    if producto is None:
        return None

    return producto["stock"]