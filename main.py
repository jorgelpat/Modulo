# from module.camper import *
# from module.camper import save
# from module.camper import delete as eliminar
import json
from os import system
import module.camper as camper
import module.trainer as trainer
from module.validate import menuNoValid
def menu():
    print("Sistema de almacenamiento de datos para campus")
    print("\t1. Informacion del camper")
    print("\t2. Informacion del trainer")
    print("\t0. Salir")
bandera=True
while (bandera):
    menu()
    opc = int(input())
    match(opc):
        case 1:
            
            with open("module/storage/camper.json", "r") as f:
                camper.camper = json.loads(f.read())
                f.close()
                system("clear")
                camper.menu()
        case 2:
            print("")
        case 0:
            system("clear")
            bandera = False
        case _:
            menuNoValid(opc)