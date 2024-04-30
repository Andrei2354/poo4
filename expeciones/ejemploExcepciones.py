class EjemploExcepciones:
    # ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int):
        if (den == 0):
            raise ZeroDivisionError("No puedes dividir por 0")
        
        return num / den


    # ValueError
    def valueError(self):
        if 10 + int("x"):
            raise ValueError("No puedes sumar una letra")

        return 10 + "x"

    # FileNotFoundError
    def fileNotFoundError(self):
        try:
            with open('archivo_que_no_existe.txt', 'r') as f:
                f.read()
        except:
            raise FileNotFoundError

    # TypeError
    def typeError(self, x:int):
        if type(x) == str:
            raise TypeError("¡Debes ingresar un número!")
       
        return type(x)
   
    # PermisionError
    def permissionError(self):
        try:
            with open('sin_permiso.txt', 'x') as f:
                f.read()
        except:
            raise PermissionError

    # IndexError
    def indexError(self):
        x = 8
        list = ["a", "b", "c", "d", "e"]
        if x >= len(list):
            raise IndexError("¡Debes ingresar una posición menor a 5!")
       
        return list[x]


    # KeyboardInterrupt
    def keyboardInterrupt(a):
        try:
            intento = input("Pulsa una tecla: ")
            if intento != KeyboardInterrupt:
                return "Finalizo con exito"
        except:
            raise KeyboardInterrupt
        
    # UnicodedecodeError
    def unicodeDecodeError(self):
        try:
            cadena = b'\xff\xfe\x00'
            cadena.decode('utf-8')
        except UnicodeDecodeError as Error:
            raise Error

    # Fuente -> https://www.boardinfinity.com/blog/untitled-8/#:~:text=In%20Python%2C%20we%20get%20an,used%20to%20solve%20the%20problem.
    # AtributeError
    def attributeError(self):
        x = 5
        x.upper()
        if x == AttributeError:
            raise AttributeError
        
        return x
