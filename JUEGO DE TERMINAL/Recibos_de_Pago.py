print(""""

##### ##### ##### ##### ##### ##### #####
#   # #     #       #   #   # #   # #
##### ###   #       #   ####  #   # #####
#  #  #     #       #   #   # #   #     #
#   # ##### ##### ##### ##### ##### #####
_______________________________________________
"""
)
import csv

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
        "1": ("Registrar recibo. ", accion1),
        "2": ("Registrar nombre. ", accion2),
        "3": ("Salir", Salir)
    }

    generar_menu(opciones, "2")

def accion1():
    recibos_pago = int(input("INGRESE EL NUMERO DE RECIBO:  "))
    nombre = input("INGRESE EL NOMBRE DE QUIEN PAGA: ")
    depto = int(input("INGRESE EL NO. DE DEPARTAMENTO. "))
    concepto = input("INGRESE EL CONCEPTO DEL PAGO: ")
    cantidad = int(input("INGRESE LA CANTIDAD DEL PAGO: "))
    
    recibo = """
    
    ########################################
    #    NUMERO DE RECIBO: {recibos_pago}
    #    NOMBRE: {nombre}
    #    CONCEPTO: {concepto}
    #    DEPARTAMENTO: {depto}
    #    CANTIDAD: {cantidad}
    ########################################
    
    """
    recibo_1 = recibo.format(recibos_pago=recibos_pago, nombre=nombre, depto=depto, concepto=concepto, cantidad=cantidad)

    print(recibo_1)

def accion2():
    print("Selecciono opcion 2")

def Salir():
    print("Saliendo")

if __name__ == '__main__':
    menu_principal()