from os import system
from module.validate import menuNoValid


def save ():
    return "Sucessfully Trainer"

def edit():
    return "Edit to trainer"

def search():
    return "The trainer is available"

def delete():
    return "Trainer delete"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del trainer")
        print("\t1. Guardar trainer")
        print("\t2. Buscar trainer")
        print("\t3. Actualizar trainer")
        print("\t4. Delete trainer")
        print("\t0. Atrás")
        opc = int(input())
        match(opc):
            case 1:
                save()
            case 2:
                search()
            case 3:
                edit()
            case 4:
                delete()
            case 0:
                system("clear")
                break
            case _:
                menuNoValid(opc)
