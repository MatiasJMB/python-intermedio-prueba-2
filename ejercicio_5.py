# •	Ejercicio 5 (18 puntos):
# Pregunte al usuario sus colores favoritos, cuando el usuario ingrese "salir" el programa debe terminar de pedir sus colores favoritos. Cree una función que imprima en mayúsculas los colores, uno por linea. Utilice kwargs o args según corresponda.


def imprimir(**kwargs):
    for key, value in kwargs.items():
        print(key, value.upper())

def main():
    lista = {}
    print("Para terminar ingrese: 'SALIR'")
    while True:
        color = input("Ingrese su color favorito: ")
        if color == "salir" or color == "Salir" or color == "SALIR":
            break
        else:
            lista[color] = color
    imprimir(**lista)

if __name__ == '__main__':
    main()

'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''
