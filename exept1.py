import random

def intDiv(a:int, b:int)->int:
    try:
        return a // b
    except:
        print("Realizamos control de cierre")



if __name__=="__main__":
    for i in range(10):
        b = random.randint(0,9)
        a = random.randint(0,9)
        print(f"A = {a} y B = {b} el resultado es: {intDiv(a, b)}")