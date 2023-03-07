print(""""

##### ##### ##### ##### ##### ##### #####
#   # #     #       #   #   # #   # #
##### ###   #       #   ####  #   # #####
#  #  #     #       #   #   # #   #     #
#   # ##### ##### ##### ##### ##### #####
_______________________________________________
"""
)

def mostrar_menu(opciones):
    print("Seleccione una opcion: ")
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while(a := input('Opcion: ')) not in opciones:
        print("Opcion incorrecta")
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        "1": ("Opcion 1", accion1),
        "2": ("Salir", Salir)
    }

    generar_menu(opciones, "2")

def accion1():
    print("Ha elegido la opcion 1")

def Salir():
    print("Saliendo")

if __name__ == '__main__':
    menu_principal()