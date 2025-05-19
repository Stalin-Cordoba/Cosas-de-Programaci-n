# Importaciones

import random
import os

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
                    
    print("-" * 10,"DEFINICIONES", "-" * 10)
    
    print("\nVector: Es un arreglo unidimensional, que se clasifica en dos subtipos:\n")
    print("1. Vector-Columna (consiste de una sóla columna, y de 'm' filas)")
    print("2. Vector-Fila (consiste de una sóla fila, y de 'n' columnas)")
    print("\nMatriz: Es un arreglo bidimensional, compuesto de filas y columnas\n")

    print("-" * 10, "TIPOS DE MATRICES", "-" * 10)

    print("\nCuadrada: Una matriz es cuadrada si tienen el mismo número de filas y columnas")
    print("Identidad: Es la matriz que actúa el elemento neutro de la multiplicación con matrices (en palabras simples, actúa como el 1)")
    print("Diagonal: Una matriz es diagonal si y sólo si los elementos por debajo y por encima de la diagonal principal son ceros")
    print("Triangular: Una matriz es triangular si los elementos por debajo o por encima de la diagonal principal son ceros. Hay 2 tipos:\n")
    print("Inferior: Una matriz es triangular inferior si los elementos por encima de la diagonal principal son ceros.")
    print("Superior: Una matriz es triangular superior si los elementos por debajo de la diagonal principal son ceros.")
    print("Singular: Una matriz es singular si no tiene inversa.")

    Continuar()
                    
    limpiarTerminal()

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
                    break

                case "0":

                    break # Aquí acaba la wea

                case _:

                    print("Ingrese una opción válida")

        if opcion == "0":

            break

main()