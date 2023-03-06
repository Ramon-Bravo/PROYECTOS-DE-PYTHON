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
    print("\n -----SELECT OPTION----- \n")
    print("\t 1. Create new payment racipt \n")
    print("\t 2. Exit. \n")

while True:
    menu()
    opcionMenu = input("Insert an option >> ")

    if opcionMenu == "1":
        print("Quieres hacer un nuevo registro?")
    elif opcionMenu == "9":
        break

