#from module.camper import *
import json
from os import system
import module.camper as camper #importa el modulo (import nombreDeCarpeta.nombreArchivo)
import module.trainer as trainer
import module.validate as validate
from module.validate import menuNoValid
#from module.camper import * #Con (*) importan todos,
#from module.camper import save, delete  
#from module.trainer import save, delete

def menu():
    print("Sistema de almacenamiento de datos")
    print("\t1.Informacion del camper")
    print("\t2.Informacion del trainer")
    print("\t0. Salir")

bandera = True
while(bandera):
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