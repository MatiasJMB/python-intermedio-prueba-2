# •	Ejercicio 4 (18 puntos):
# Resuelva los siguientes bloques de código añadiendo las sentencias Try/Except que considere necesarias. Si el bloque de código no tiene errores, imprima "El bloque de código no tiene errores" en la consola y el resultado del bloque según corresponda. Si el bloque de código tiene errores, imprima el error en la consola. El ejercicio se encuentra adjunto a la tarea.

def bloque_1():
    try:
        mi_lista = ["Python","C","C++","JavaScript"]
        print(mi_lista[5])
    except IndexError:
        print("El índice excede el largo total de la lista")

def bloque_2(num):
    try:
        resultado = num + 10
        print(resultado)
    except TypeError:
        print("El tipo de dato ingresado no es correcto")

def bloque_3():
    try:
        capitales  = {
            "Colombia": "Bogotá",
            "Argentina": "Buenos Aires",
            "Perú": "Lima",
            "Chile": "Santiago de Chile",
        }
        print(capitales["Brasil"])
    except KeyError:
        print("El elemento del diccionario al cual se quiere acceder no existe")
    
        

def main():
    # Esta función no debe ser modificada. Modifique las funciones bloque_1, bloque_2, bloque_3 y bloque_4.
    # Si modifica esta sección para hacer pruebas recuerde cambiarla antes de enviar el ejercicio.
    print("Bloque 1")
    bloque_1()
    print("-------------")

    print("Bloque 2")
    bloque_2("dos")
    print("-------------")

    print("Bloque 3")
    bloque_3()
    print("-------------")

if __name__ == '__main__':
    main()
    
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''
