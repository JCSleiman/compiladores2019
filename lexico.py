# Los estados del 0 al 11 serán funciones, y dependiendo de la funcion en la que nos encontremos en ese
# momento revisaremos la matriz y le asignaremos el estado que tiene.
# ord() function para sacar el código ascii de un caracter


""" [[XYZ -> es un string],
[. -> es un punto],
[8045 -> es un entero],
[400.55 -> es un decimal],
[hola -> es un string]] """

import re
stringFinal = []
""" matriz = [[0,1,2,3,4,5,6,7,8,9,10,11], # Estados iniciales
          [1,1,3,3,4,204,207,209,211,213,215,217], # Estados para los números
          [4,200,300,201,4,204,207,209,211,213,215,217], # Estados para letras
          [5,200,300,201,202,204,206,209,211,213,215,217], # >
          [6,200,300,201,202,204,207,209,211,213,215,217], # <
          [9,200,300,201,202,203,205,209,211,212,214,217], # =
          [7,200,300,201,202,204,207,208,211,213,215,217], # +
          [8,200,300,201,202,204,207,209,210,213,215,217], # -
          [404,200,300,201,202,204,207,209,211,213,215,217], # *
          [11,200,300,201,202,204,207,209,211,213,215,216], # /
          [10,200,300,201,202,204,207,209,211,213,215,217], # !
          [404,200,300,201,202,204,207,209,211,213,215,217], # %
          [404,200,300,201,202,204,207,209,211,213,215,217], # #
          [404,200,300,201,202,204,207,209,211,213,215,217] # .
        ] # Los "404" son los vacíos """

matriz = [# Estados iniciales
          [0,1,4,5,6,9,7,8,404,11,10,404,404,404], 
          [1,1,200,200,200,200,200,200,200,200,200,200,200,200], # Estados para los números
          [2,3,300,300,300,300,300,300,300,300,300,300,300,300], # Estados para letras
          [3,3,201,201,201,201,201,201,201,201,201,201,201,201], # >
          [4,4,4,202,202,202,202,202,202,202,202,202,202,202], # <
          [5,204,204,204,204,203,204,204,204,204,204,204,204,204], # =
          [6,207,207,206,207,205,207,207,207,207,207,207,207,207], # +
          [7,209,209,209,209,209,208,209,209,209,209,209,209,209], # -
          [8,211,211,211,211,211,211,210,211,211,211,211,211,211], # *
          [9,213,213,213,213,212,213,213,213,213,213,213,213,213], # /
          [10,200,300,201,202,204,207,209,211,213,215,217], # !
          [11,200,300,201,202,204,207,209,211,213,215,217] # %
        ] # Los "404" son los vacíos

""" if char == '+':
    EDO=7
    [6][EDO] """
    #matriz[EDO][]
def main():

    def edo1(chartr):
        
        while True:
            if chartr.isdigit():
                print(chartr+" es un número!")
    
    def edo2(char):
        return ""
    
    def edo3(char):
        return ""
    
    def edo4(char):
        return ""
    
    def edo5(char):
        return ""
    
    def edo6(char):
        return ""
    
    def edo7(char):
        return ""
    
    def edo8(char):
        return ""
    
    def edo9(char):
        return ""
    
    def edo10(char):
        return ""
    
    def edo11(char):
        return ""
    
    def edo211(char):
        return ""

    with open("fuente.txt","r") as f:
        while True:
            if f.mode == "r":
                f.readline()
                EDO = 0
                caracter = 0
                caracter = caracter + 1
                cadena = cadena + caracter
                EDO = matriz[EDO,COLUMNA]
                for line in f: # aquí leemos la linea completa
                    for chartr in line: # e iteramos la linea caracter por caracter
                        """ aquí leemos cada caracter de la linea
                        y se empezará el procesamiento de los estados caracter por caracter """
                        ascii = ord(chartr)
                        if ascii >= 48 and ascii <= 57:
                            print("El caracter "+ chartr +" es: dígito")
                        elif ascii >= 65 and ascii <= 90 or ascii >= 97 and ascii <= 122:
                            print("El caracter "+ chartr +" es: letra")
                        elif ascii == 62:
                            print("El caracter "+ chartr +" es: '>'")
                        elif ascii == 60:
                            print("El caracter "+ chartr +" es: '<'")
                        elif ascii == 61:
                            print("El caracter "+ chartr +" es: '='")
                        elif ascii == 43:
                            print("El caracter "+ chartr +" es: '+'")
                        elif ascii == 45:
                            print("El caracter "+ chartr +" es: '-'")
                        elif ascii == 42:
                            print("El caracter "+ chartr +" es: '*'")
                        elif ascii == 47:
                            print("El caracter "+ chartr +" es: '/'")
                        elif ascii == 33:
                            print("El caracter "+ chartr +" es: '!'")
                        elif ascii == 37:
                            print("El caracter "+ chartr +" es: '%'")
                        elif ascii == 35:
                            print("El caracter "+ chartr +" es: '#'")
                        elif ascii == 46:
                            print("El caracter "+ chartr +" es: '.'")
                        elif ascii == 32:
                            print("El caracter '"+ chartr +"' es: 'espacio'")


            break # interrumpe el programa cuando termina de leer las lineas
    f.close() # Cerrar el archivo a leer 

matriz_estados ={200: "enteros"}
if __name__ == "__main__":
    main()