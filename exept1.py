import random

def intDiv(a:int, b:int)->int:
    try:
        return a // b
    except TypeError:
        print('TypeError: Check operands. Some of them seems strange...')
    except ZeroDivisionError:
        print('ZeroDivisionError: Please do not divide by zero...')      
    except:
        print("Realizamos control de cierre")



if __name__=="__main__":

    def main()-> None:
        for i in range(10):
            b = random.randint(0,9)
            a = random.randint(0,9)
            print(f"A = {a} y B = {b} el resultado es: {intDiv(a, b)}")

        try:
            intDiv()
        except:
            intDiv(2,"3")

    main()