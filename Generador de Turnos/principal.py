import numeros

def preguntar():
    print("Bienvenidos a Farmacia Python!!")
    while True:
        print("[P] - Perfumeria \n[F] - Farmacia \n[C] Cosmetica")
        try:
            mi_rubro= input("Elija su rubro: ").upper()
            ['P','F', 'C'].index(mi_rubro)
        except ValueError:
            print("No es una opcion valida")
        else:
            break
    numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno= input("Deseas otro turno? [S] [N}").upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print("No es una opcion valida")
        else:
            if otro_turno == 'N':
                print("Gracias por su visita a Faramacia Python!!")
                break

inicio()