import pandas as pd
from datetime import datetime
import openpyxl
from tabulate import tabulate

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
    while (a := input('Opcion: ')) not in opciones:
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

    class Recibo:

        def __init__(self):
            self.recibos = []

        def captura(self):
            continuar = True
            while continuar:
                folio = str(input("Ingrese el folio: "))
                fecha = datetime.now().date()
                depto = str(input("Ingrese el departamento: "))
                nombre = input("Ingrese el nombre: ")
                monto = int(input("Ingrese el monto del pago: "))
                concepto = input("Ingrese el concepto del pago: ")

                recibo = {
                    "Folio": folio,
                    "Fecha": fecha,
                    "Departamento": depto,
                    "Nombre": nombre,
                    "Monto": monto,
                    "Concepto": concepto
                }
                self.recibos.append(recibo)
                respuesta = input("¿Quiere ingresar otro recibo?")

                if respuesta.lower() != "s":
                    continuar = False

            self.guardar_excel()

        def guardar_excel(self):
            datos = {
                "Folio": [],
                "Fecha": [],
                "Departamento": [],
                "Nombre": [],
                "Monto": [],
                "Concepto": []
            }
            for recibo in self.recibos:
                datos["Folio"].append(recibo["Folio"])
                datos["Fecha"].append(recibo["Fecha"])
                datos["Departamento"].append(recibo["Departamento"])
                datos["Nombre"].append(recibo["Nombre"])
                datos["Monto"].append(recibo["Monto"])
                datos["Concepto"].append(recibo["Concepto"])

            df = pd.DataFrame(datos)
            nombre_archivo = input("Ingrese el nombre del archivo de Excel: ")
            df.to_excel(nombre_archivo + ".xlsx", index=False)
            print("Los recibos se han guardado en el archivo",
                  nombre_archivo + ".xlsx")

    clase = Recibo()
    clase.captura()


def accion2():
    print("En trabajo")


def Salir():
    print("Saliendo")
    exit()


if __name__ == '__main__':
    menu_principal()
