# Crear un código con la exepción IndexError

def resultadoLista(list)->int:
    list = [1, 2, 3]
    almacen = list
    try:
          return almacen[3]
    except IndexError:
        return IndexError

