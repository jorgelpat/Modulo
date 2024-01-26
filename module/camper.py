from os import system
from .data import camper
from module.validate import menuNoValid
def save (nombre):
    camper.append(nombre)
    return f"Sucessfully Camper{nombre}"

def edit():
    return "Edit to camper"

def search():
    return "The camper is available"

def delete():
    return "Camper delete"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del camper")
        print("\t1. Guardar camper")
        print("\t2. Buscar camper")
        print("\t3. Actualizar camper")
        print("\t4. Delete camper")
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

