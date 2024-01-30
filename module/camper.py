from os import system
import json
from .data import camper, generos
from module.validate import menuNoValid
def save ():
    info = {
        "Nombre": input("Ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese apellido del camper\n"),
        "Edad": input("Ingrese la edad del camper\n"),
        "Genero": input("Elija su genero:\n\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    camper.append(info)
    with open("module/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Camper"

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

