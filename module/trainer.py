from os import system
import json
from module.validate import menuNoValid
from .data import trainer, generos


def save ():
    info = {
        "Nombre": input("Ingrese el nombre del trainer\n"),
        "Apellido": input("ingrese el apellido del trainer\n"),
        "Edad": int(input("ingrese la edad del trainer\n")),
        "Género": input("Elija su género\n\t"+"\t".join([f"{generos.index(i)+1}.{i}\n" for i in sorted(generos)]))
    }
    trainer.append(info)
    with open("module/storage/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
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
