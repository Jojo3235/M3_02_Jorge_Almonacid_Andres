#Ejercicio 2

lista = [4,7,30,23,5]   #Definimos una lista

def non_list_element():    #Creamos una función para capturar la excepción que se nos pide
    try:
        lista[10]       #Buscamos un elemento no perteneciente a la lista
    except IndexError:      #Capturamos el error
        return "No existe ese elemento dentro de la lista"  #Decimos que no existe ese elemento en la lista

def main():     #Creamos la función main
    print(non_list_element())

if __name__ == "__main__":  #Ejecutamos el código
    main()