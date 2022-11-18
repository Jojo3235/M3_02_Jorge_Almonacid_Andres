from Ejercicio1 import main as m1
from Ejercicio2 import main as m2
from Ejercicio3 import main as m3
from Ejercicio4 import main as m4           #Importamos las funciones

def main():             #Las juntamos en una misma función final
    m1()
    m2()
    m3()
    m4()

if __name__ == "__main__":      #Creamos el ejecutor
    print("Se ha ejecutado el módulo")
    main()
else:
    print("Se ha importado el módulo")