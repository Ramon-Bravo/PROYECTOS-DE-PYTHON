import signal

print(""""

##### ##### ##### ##### ##### ##### #####
#   # #     #       #   #   # #   # #
##### ###   #       #   ####  #   # #####
#  #  #     #       #   #   # #   #     #
#   # ##### ##### ##### ##### ##### #####
_______________________________________________
"""
)

def menu():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("\n -----SELECT OPTION----- \n"))
            correcto = True
        except ValueError:
            print("Error, introduzca un numero. ")
        return num
salir = False
opcion = 0

while not salir:
    print("\n 1. Capturar nuevo recibo de pago. \n")
    print("\n 2. Salir. \n")

    opcion = menu
        
    if opcion == 1:
        print("Quieres hacer un nuevo registro?")
        input("Haz pulsado la opcion 1...")
    elif opcion == 2:
        salir = True
    else:
        print("Introduzca un numero.")

input('Press <ENTER> to continue')

def signal_handler(signal_number, frame):
    print ("Proceed ...")

signal.signal(signal.SIGINT, signal_handler)
signal.pause()

