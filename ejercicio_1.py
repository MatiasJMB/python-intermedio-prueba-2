# Ejercicio 1 (18 puntos): 
# Pedro, Juan y María son 3 estudiantes de un colegio, cada uno de ellos tiene las notas de
# sus ramos en una lista ordenadas de la siguiente forma: Historia, Lenguaje, Matemáticas,
# Física, Química y Biología. Escriba un programa que reciba las 3 listas y devuelva una nueva
# lista con el promedio de cada estudiante. Por ejemplo, si Pedro tiene las notas [4, 5, 6, 7, 4,
# 3], Juan tiene las notas [5, 6, 4, 3, 3, 3] y María tiene las notas [6, 6, 5, 4, 3, 3], el programa
# debe devolver [5.0, 5.66, 5.0, 4.66, 3.33, 3.0]. Redondee los promedios a 2 decimales. Utilice
# lambda, map, filter o reduce según corresponda.
# Muestre el promedio de cada asignatura de los 3 estudiantes de la siguiente forma por la
# consola:
# Historia: 5.0
# Lenguaje: 5.66
# Matemáticas: 5.0
# Física: 4.66
# Química: 3.33
# Biología: 3.0

def main():
    pedro = [4,5,6,7,4,3]
    juan = [5,6,4,3,3,3]
    maria = [6,6,5,4,3,3]
    promedio = []
    promedio = list(map(lambda a: (a[0] + a[1] + a[2]) / 3, zip(pedro,juan,maria))) 
    redondear = list(map(lambda a: round(a, 2), promedio))
    print(redondear)
    print("Historia:", redondear[0],"\nLenguaje:", redondear[1] ,"\nMatemáticas:", redondear[2] , "\nFísica:", redondear[3], "\nQuímica:", redondear[4],"\nBiología:", redondear[5])
    

if __name__ == '__main__':
    main()
    
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''