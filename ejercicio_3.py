# •	Ejercicio 3 (18 puntos):
# Cree una calculadora que reciba una lista de numeros. Utilice función lambda, map, filter o reduce según corresponda. Imprima el resultado por la consola.

# Por ejemplo, si la lista es [2, 3, 4, 5, 6], el programa debe devolver:
# Suma: 20
# Resta: -16
# Multiplicación: 720
# División: 0.001388888888888889
# Exponente: 2348542582773833227889480596789337027375682548908319870707290971532209025114608443463698998384768703031934976
# Raiz cuadrada: 1.001927263624698
from functools import reduce

def main():
    numeros = [2,3,4,5,6] 
    suma = reduce(lambda a, b: a + b, numeros)
    resta = reduce(lambda a, b: a - b, numeros)
    multiplicacion = reduce(lambda a, b: a * b, numeros)
    division = reduce(lambda a, b: a / b, numeros)
    exponente = reduce(lambda a, b: a ** b, numeros)
    raiz = reduce(lambda a, b: a ** (1/b), numeros)

    print("Suma:",suma,"\nResta:",resta,"\nMultiplicacion:",multiplicacion,"\nDivision:",division,"\nExponente:",exponente,"\nRaiz:",raiz)

if __name__ == '__main__':
    main()
    
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''