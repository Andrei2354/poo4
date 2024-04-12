# Crear un código con la exepción IndexError

def resultadoLista(list)->int:
    almacen = list
    try:
          print(almacen[3])

    except IndexError:
        print("Valores fuera de rango")

if __name__=="__main__":

    def main()-> None:
        list = [1, 2, 3]
        list = [1, 2, 3, 5, 6]
        resultadoLista(list)

    main()