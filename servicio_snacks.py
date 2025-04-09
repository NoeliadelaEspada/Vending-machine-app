                                # Servicio snacks
import os.path 
from snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []          
        if os.path.isfile(self.NOMBRE_ARCHIVO): 
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [ 
            Snack('Patatas fritas Ruffles', 50),    
            Snack('Kinder Bueno', 80),
            Snack('Zumo Bifrutas', 30),
            Snack('Sandwhich huevo/atún', 130)
        ]
        self.snacks.extend(snacks_iniciales) 
        self.guardar_snacks_archivo(snacks_iniciales) 

    def guardar_snacks_archivo(self, snacks): 
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo: 
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n') 
        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')

    def obtener_snacks(self): 
        snacks = []  
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:  
                    id_snack, nombre, precio = linea.strip().split(',') 
                    snack = Snack(nombre, float(precio)) 
                    snacks.append(snack) 
        except Exception as e:
            print(f'Error al leer archivo de snacks: {e}')
        return snacks   


    def agregar_snack(self,snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('--- Snacks en el inventario ---')
        for snack in self.snacks:  
            print(snack)

    def get_snacks(self):  
        return self.snacks


Pero primero definiremos el método obtener snacks. Este cargará en memoria cada
uno de los snacks de nuestro archivo. Así que solo leerá el archivo y los cargará de ahí.

"""
