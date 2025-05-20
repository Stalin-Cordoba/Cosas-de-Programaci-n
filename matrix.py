# Importaciones

import cmath
import math
import os
import random

# Los weones culiaos que guardan todo

ListaVectores = []
ListaMatrices = []

# -----------------
# ----Funciones----
# -----------------

# Funciones misceláneas

def limpiarTerminal(): # Literalmente limpia la terminal xddddddddd
    
    os.system('cls' if os.name == 'nt' else 'clear')

def Continuar():

    print("\nIngrese cualquier letra para continuar")
    ok = input()

def eleccionNumero():

    while True:

        num = int(input())

        if num <= 0:

            print("Ingrese un entero positivo")
        else:
            
            break

    return num

def Contexto():

    limpiarTerminal()
    
    while True:

        print("-" * 5, "Escoge las cosas que deseas saber el contexto", "-" * 5)
        print("Nota: La información incluida aquí es meramente la elemental, si deseas saber más acerca sobre los procedimientos, además de ver ejemplos, puedes verlo en la wiki del repositorio.")
        print("\n1) Definiciones generales")
        print("2) Condiciones para realizar las operaciones")
        print("3) Volver al menú")

        while True:

            elegir = input()

            match elegir:

                case "1":

                    limpiarTerminal()

                    print("-" * 10, "DEFINICIONES GENERALES", "-" * 10)
                    print("\n1. Vector: Es un arreglo unidimensional con 'n' elementos. Hay 2 tipos de vectores:\n")
                    print("1.1 Vector-columna: Es un vector compuesto de una sóla columna y de 'n' filas.")
                    print("1.2 Vector-fila: Es un vector compuesto de una sóla fila, y de 'n' columnas.\n")
                    print("2. Escalar: Es un término que simplemente se refiere a un número (o constante) cualquiera.")
                    print("3. Matriz: Es un arreglo bidimensional que está compuesto de 'm' filas por 'n' columnas.\nAquí están los tipos de matrices más conocidos:\n")
                    print("3.1 Matriz cuadrada: Es una matriz en el que el número de filas, es igual al número de columnas.")
                    print("3.2 Matriz diagonal: Es una matriz en donde los componentes fuera de la diagonal principal (la diagonal principal son los componentes que van desde la esquina izquierda, hasta la esquina derecha) son todos cero.")
                    print("3.3 Matriz identidad: Es una matriz diagonal que actúa como el elemento neutro de la multiplicación de matrices (en palabras simples, actúa como el 1). Su diagonal principal está compuesta solamente de unos.")
                    print("3.4 Matriz triangular: Es una matriz en donde los elementos que estén por debajo o por encima de la diagonal principal son cero. Hay 2 tipos:\n")
                    print("3.4.1 Triangular inferior: Matriz en donde los elementos situados por encima de la diagonal principal son cero.")
                    print("3.4.2 Triangular superior: Matriz en donde los elementos situados por encima de la diagonal principal son cero.\n")
                    print("3.5 Matriz cero: Valga la redundancia, es una matriz en donde todos elementos son cero.")
                    print("3.6 Matriz singular: Es una matriz que no es invertible (o sea, no tiene inversa). En caso de que tenga inversa, es una matriz invertible.")
                    print("3.7 Matriz transpuesta: Es una matriz que se obtiene al intercambiar las filas con las columnas.")
                    print("3.8 Matriz simétrica: Es una matriz cuya transpuesta, es igual a la matriz original.")
                    print("3.9 Matriz antisimétrica: Es una matriz cuya transpuesta, es igual a la matriz original, pero en negativo.")
                    print("3.10 Matriz ortogonal: Es una matriz cuya transpuesta, es igual a la inversa de la matriz original.")
                    print("3.11 Matriz elemental: Es una matriz diagonal que es equivalente a una operación de la eliminación de Gauss-Jordan.\n")
                    print("4. Determinante: Es una escalar que se utiliza para ciertos cálculos con matrices, como por ejemplo el cálculo de la inversa.")

                    Continuar()

                    limpiarTerminal()
                    
                    break

                case "2":

                    limpiarTerminal()
                    
                    print("-" * 10, "CONTEXTO SOBRE LAS OPERACIONES DE ESTA MIERDA", "-" * 10)

                    print("1. Suma o resta de vectores: Para sumar o restar dos vectores, los dos deben tener la misma cantidad de elementos.")
                    print("2. Producto de dos vectores: La misma condición que en la suma y resta, con la diferencia de que el resultado será una escalar.")
                    print("3. Suma o resta de matrices: Para sumar o restar dos matrices, las dos deben ser del mismo tamaño.")
                    print("4. Producto de dos matrices: Para poder multiplcar dos matrices, primero, el número de columnas de la primera matriz, debe ser igual al número de filas de la segunda matriz. El resultado será una matriz, cuyas dimensiones serán:\n")
                    print("N° de filas: Será igual al número de filas que tiene la primera matriz")
                    print("N° de columnas: Será igual al número de columnas de la segunda matriz\n")

                    Continuar()

                    limpiarTerminal()
                    break

                case "3":
                    
                    break

                case _:

                    print("Ingrese una opción válida")

        if elegir == "3":

            break

# Funcione para las operaciones con vectores

def elementosVector(númeroElementos):

    vector = []
    
    for i in range(númeroElementos):

        vector.append(random.randint(-50, 50))

    return vector

def imprimirVectores():

    if len(ListaVectores) == 0:

        print("No hay nada we")
    else:

        for i in ListaVectores:

            print(i)

def elegirOperacionVector():

    print("Operaciones que puedes hacer:\n")
    print("1) Suma de vectores")
    print("2) Resta de vectores")
    print("3) Multiplicación de vectores")
    print("4) Volver al menú")
    print("Elige una opción pa")

    while True:

        opcion = input()

        match opcion:

            case "1":

                limpiarTerminal()

                imprimirVectores()
                print("Elija los vectores mi loco")

                vec1 = eleccionNumero()
                vec2 = eleccionNumero()

                if vec1 > len(ListaVectores) or vec2 > len(ListaVectores):

                    print("Usted pendejo eligió uno o dos vectores que no existen (Fuera de rango)")
                    Continuar()
                elif len(ListaVectores[vec1 - 1]) != len(ListaVectores[vec2 - 1]):

                    print("No se puede realizar la operación porque los vectores no tienen la misma cantidad de elementos")
                    Continuar()
                else:

                    print("Resultado:")
                    print(sumarVectores(ListaVectores[vec1 -1], ListaVectores[vec2 -1]))
                    Continuar()
                
                break

            case "2":

                limpiarTerminal()

                imprimirVectores()
                print("Elija los vectores mi loco")

                vec1 = eleccionNumero()
                vec2 = eleccionNumero()

                if vec1 > len(ListaVectores) or vec2 > len(ListaVectores):

                    print("Usted pendejo eligió uno o dos vectores que no existen (Fuera de rango)")
                    Continuar()
                elif len(ListaVectores[vec1 - 1]) != len(ListaVectores[vec2 - 1]):

                    print("No se puede realizar la operación porque los vectores no tienen la misma cantidad de elementos")
                    Continuar()
                else:

                    print("Resultado:")
                    print(restarVectores(ListaVectores[vec1 -1], ListaVectores[vec2 -1]))
                    Continuar()

                break

            case "3":

                limpiarTerminal()

                imprimirVectores()
                print("Elija los vectores mi loco")

                vec1 = eleccionNumero()
                vec2 = eleccionNumero()

                if vec1 > len(ListaVectores) or vec2 > len(ListaVectores):

                    print("Usted pendejo eligió uno o dos vectores que no existen (Fuera de rango)")
                    Continuar()
                elif len(ListaVectores[vec1 - 1]) != len(ListaVectores[vec2 - 1]):

                    print("No se puede realizar la operación porque los vectores no tienen la misma cantidad de elementos")
                    Continuar()
                else:

                    print("Resultado:")
                    print(multiplicarVectores(ListaVectores[vec1 -1], ListaVectores[vec2 -1]))
                    Continuar()
                
                break

            case "4":

                break

            case _:

                print("Elige una opción válida")

def sumarVectores(vector1, vector2):

    sumaTotal = []

    for i in range(0, len(vector1)):

        sumaTotal.append(vector1[i] + vector2[i])

    return sumaTotal

def restarVectores(vector1, vector2):

    restaTotal = []

    for i in range(0, len(vector1)):

        restaTotal.append(vector1[i] - vector2[i])

    return restaTotal

def multiplicarVectores(vector1, vector2):

    productoTotal = 0
    
    for i in range(0, len(vector1)):

        productoTotal += (vector1[i] * vector2[i])

    return productoTotal

# Funciones para los matrices

def elegirOperacionMatrix():

    print("Elija una operación mi loco\n")
    print("1) Suma de matrices")
    print("2) Resta de matrices")
    print("3) Multiplicación de matrices")
    print("4) Eliminación por Gauss-Jordan")
    print("5) Cálculo de la inversa")
    print("6) Cálculo de la determinante")
    print("7) Volver al menú")

def elementosMatriz(filas, columnas):

    matriz = []

# --------------------
# ----Función main----
# --------------------

def main():

    while True:

        print("Bienvenido a esta mierda\n")
        print("1) Creación de vectores")
        print("2) Mostrar vectores")
        print("3) Operaciones con vectores")
        print("4) Creación de Matrices")
        print("5) Mostrar matrices")
        print("6) Operaciones con matrices")
        print("7) Contexto para algunas cositas (uwu)")
        print("0) Salir\n")
        print("Ingrese una opción\n")

        while True:

            opcion = input()

            match opcion:

                case "1": # Desde aquí empieza la onda

                    limpiarTerminal()
            
                    print("¿De cuántos elementos desea que sea el vector?")
                    print("(Nota: Por el momento, los elementos del vector van a ser aleatorios, en un intervalo de -50 a 50)")

                    ListaVectores.append(elementosVector(eleccionNumero()))
                    print("Resultado:")
                    print(ListaVectores[len(ListaVectores) - 1])

                    Continuar()

                    limpiarTerminal()

                    break # Aquí acaba la onda
                
                case "2": # Desde aquí empieza la onda

                    limpiarTerminal()

                    print("<---LISTA DE VECTORES--->\n")
                    imprimirVectores()
                    Continuar()

                    limpiarTerminal()

                    break # Aquí acaba la onda
                case "3":

                    limpiarTerminal()
                    
                    if len(ListaVectores) <= 1:

                        print("Sólo hay un vector, o no hay vectores en lo absoluto")
                        Continuar()
                    else:
                    
                        elegirOperacionVector()
                    
                    limpiarTerminal()

                    break

                case "4":

                    limpiarTerminal()
                    
                    print("A1")
                    Continuar()
                    
                    limpiarTerminal()
                    break

                case "5":

                    limpiarTerminal()
                    
                    print("A1")
                    Continuar()
                    
                    limpiarTerminal()
                    break

                case "6":

                    limpiarTerminal()
                    
                    print("A1")
                    Continuar()
                    
                    limpiarTerminal()
                    break

                case "7":

                    Contexto()
                    limpiarTerminal()
                    break

                case "0":

                    break # Aquí acaba la wea

                case _:

                    print("Ingrese una opción válida")

        if opcion == "0":

            limpiarTerminal()
            break

main()