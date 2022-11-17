# •	Ejercicio 2 (18 puntos):
# Cree una función que determine si un numero es primo o no. Calcule los numeros primos del 1 al 1000. Solo la función para determinar que es primo puede llevar un for, el resto debe ser con lambda, map, filter o reduce. Imprima la lista por la consola.

def primo(numero):
    for i in range(2, numero):
       if numero % i == 0:
            return False
    return True

def main():
    primos = list(filter(lambda a: primo(a), range(1, 1001)))
    print(primos)

if __name__ == '__main__':
    main()
    
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''