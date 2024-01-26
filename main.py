#from module.camper import *
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
            system("clear")
            camper.menu()
        case 2:
            system("clear")
            trainer.menu()
        case 0:
            break
        case _:
            menuNoValid(opc)