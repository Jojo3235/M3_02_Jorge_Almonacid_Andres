#Ejercicio 3

def error_concat():     #Creamos una función para detectar errores de tipo TypeError
    try:   
        resultado = "2" + 10    #Intentamos sumar la cadena y el número
    except TypeError:   #Si salta un excepción de este tipo 
        return "No se puede sumar una cadena a un número"   #Decimos que no se puede sumar una cadena y un número
    return resultado
    
def main():         #Creamos la función main
    print(error_concat())

if __name__ == "__main__":  #Ejecutamos el código
    main()