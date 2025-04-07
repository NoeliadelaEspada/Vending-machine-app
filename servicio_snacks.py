                                # Servicio snacks
import os.path #habría que importar el paquete os.path
from snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt' # Creamos un archivo donde se almacenará la información de los snacks de nuestra app.


    def __init__(self): #añadimos el constructor de la clase, sin parámetros
        self.snacks = []           # Este atributo creará un lista vacía donde irán nuestros snacks
        if os.path.isfile(self.NOMBRE_ARCHIVO):  #Si la lista de snacks ya existe, entonces la obtendremos del archivo ya creado (nombre_archivo)
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [ 
            Snack('Patatas fritas Ruffles', 50),     # Y en esta lista empezamos a crear objetos de la clase snack con sus parámetros (nombre y precio)
            Snack('Kinder Bueno', 80),
            Snack('Zumo Bifrutas', 30),
            Snack('Sandwhich huevo/atún', 130)
        ]
        self.snacks.extend(snacks_iniciales) #Así anexamos los snacks iniciales a la lista de snacks principal.
        # Esta información está guardada en memoria, pero queremos guardarla en el archivo así que llamamos al método siguiente:
        self.guardar_snacks_archivo(snacks_iniciales) # Y guardamos los snacks iniciales

    def guardar_snacks_archivo(self, snacks): #Como parametros recibiremos una lista, que es la que queremos guardar en el archivo
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo: # Abrimos nuestro archivo en modo añadir, en caso de que no se haya creado ya, se crea y se añade.
                for snack in snacks: #Con un ciclo for iteramos para que se escriban todos los elementos
                    archivo.write(f'{snack.escribir_snack()}\n') #y con el método write escribimos el snack, con el método escribir snack.
        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')
        
    # Añadimos un bloque de try-except en caso de que ocurra algún fallo

    def obtener_snacks(self): 
        snacks = []  #Definimos una lista vacía
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo: #leemos nuestro archivo
                for linea in archivo:  # Leemos el archivo usando un ciclo for
                    id_snack, nombre, precio = linea.strip().split(',') #Usamos el método strip para quitar saltos de lina y split para separar los snacks con comas.
                    # Todo esto lo almacenamos en las variables id_snack, nombre y precio
                    snack = Snack(nombre, float(precio))  #Creamos un objeto snack, que proviene de la clase snacks y convertimos el precio a float.
                    snacks.append(snack) #añadimos el snack a nuestra lista
        except Exception as e:
            print(f'Error al leer archivo de snacks: {e}')
        return snacks   #Devolvemos la lista de snacks en caso de que ya hayamos cargado la información, sino será una lista vacía.


    def agregar_snack(self,snack):
        self.snacks.append(snack) # Utilizando nuestra lista de snacks (el atributo de clase), llamamos al método append y utilizamos como parámetro snack. 
        self.guardar_snacks_archivo([snack])
# Y de esta forma, añadimos snack también como argumento del método)
# Pero no solo hay que añadirlo a la lista en memoria, sino tambien al archivo.
# Para ello, llamamos al método guardar_snacks_archivo y dentro de este crearemos añadiremos
#snack pero entre corchetes, para que sea una lista y pueda ser procesada por el método.

    def mostrar_snacks(self):
        print('--- Snacks en el inventario ---')
        for snack in self.snacks:  #recorremos todos los elementos que están en el atributo de clase
            print(snack)

    def get_snacks(self):  # Método getter que devuelve el atributo de clase snacks
        return self.snacks









""" 
Vamos a revisar si ya existe el archivo de snacks.
Si ya existe, obtenemos los snacks del archivo.
Sino, cargamos algunos snacks iniciales.

Para revisar si ya existe el archivo, podemos utilizar el condicional
if junto con la expresión os.path.isfile. 
Os significa Operating system, que es el nombre de un paquete.
Path es una variable a través de la cual se puede acceder al método
isfile()

Si efectivamente existe, vamos a inicializar la lista de snacks: self.snacks. 
Para ello, llamaremos al método obtener snacks()

En caso de que no exista la lista anteriormente, la crearemos y cargaremos
snacks de manera inicial, con el método, cargar_snacks_iniciales().

como el archivo snacks.txt aún no existe seguiremos programando
el else en caso de que no haya un archivo y cargaremos los snacks iniciales.
Entonces, en el método de los snacks iniciales, creamos una lista y con la ayuda 
de la clase snack, vamos a crear algunos.
una vez hemos añadido y creado la lista de snacks iniciales, las vamos a anexar a nuestra lista oficial.

Ahora vamos a completar el código en caso de que ya exista el archivo.
Pero primero definiremos el método obtener snacks. Este cargará en memoria cada
uno de los snacks de nuestro archivo. Así que solo leerá el archivo y los cargará de ahí.

"""
