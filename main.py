from Ejercicio1 import division_por_cero        #Importamos todas las funciones de los módulos
from Ejercicio2 import non_list_element
from Ejercicio3 import non_dict_key
from Ejercicio4 import error_concat

if __name__ == "__main__":  #Ejecuto el código global con todas las funciones definidas en los otros archivos
    print(division_por_cero())
    print(non_list_element())
    print(non_dict_key())
    print(error_concat())