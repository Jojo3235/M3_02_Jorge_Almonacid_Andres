#Ejercicio 1

def division_por_cero():    #Creo una función donde meto el código pedido por el ejercicio
    try:                    #Intento correrlo
        7/0
    except ZeroDivisionError:   #Como es una división entre 0 usamos este error para que salte
        return "No se puede dividir entre 0"    #Decimos que devuelva el siguiente mensaje

if __name__ == "__main__":      #Ejecutamos el código
    print(division_por_cero())