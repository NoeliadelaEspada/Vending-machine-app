from servicio_snacks import ServicioSnacks
 #importamos la clase servicio_snacks para poder usar sus métodos.
from snack import Snack # importamos la clase snack para poder crear un objeto.

class MaquinaSnacks: 
    def __init__(self):   # creamos el constructor de esta clase, el cual tendrá una referencia del objeto servicio_snacks.
        self.servicio_snacks = ServicioSnacks() # Para poder usarlo en cualquier momento crearemos un objeto de este tipo. 
                                                # Con esta variable podremos llamar a los métodos de la clase servicio_snacks.
        self.productos = [] #Creamos una variable donde se encuentra una lista en la que se irán almacenando los productos que compremos, para crear un ticket de compra.
    
    def maquina_snacks(self):   # método para generar el menú.
        salir = False # creamos la variable salir, con el valor inicial de falso
        print('**** Maquina de snacks ****')
        self.servicio_snacks.mostrar_snacks() #Llamamos al método servicios_snacks, con el que accederemos al método de su clase mostrar_snacks
        while not salir: # Creamos un bucle, mientras que salir no sea verdadero
            try:
                opcion = self.mostrar_menu() # Creamos la variable opción, donde se almacena un método para mostrar el menú
                salir = self.ejecutar_opcion(opcion) # Creams la variable salir, donde se almacena un método de ejecutar la opción elegida.
               # Según la opción que seleccione el usuario, le pasamos como parámetro la opción seleccionada. Y además este método no solo ejecutará las acciones seleccionadas sino que también devolverá el valor salir.
               # Si el usuario ha seleccionado el valor salir, entonces la variable salir cambia su valor a verdadero.
            except Exception as e:
                print(f'Ocurrió un error: {e}') # En caso de que alguna de las opciones del menú no sea válida.

    
    def mostrar_menu(self):  # Definimos el método mostrar menu, con una cadena multilínea ("""""")
        print(f'''Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar nuevo snack al inventario
        4. Mostrar el inventario de snacks
        5. Salir ''')
        return int(input('Elige una opción: ')) # A través de un input le pedimos al usuario que seleccione una opción, esta seleccion deberá ser de tipo entero.
     # Este método almacenará en la variable opción un valor de tipo entero, es decir, una de las opciones de la lista


    def ejecutar_opcion(self, opcion): # Este método recibirá el parámetro opción
        if opcion == 1:   # Creamos condicionales para cada opción que se elija
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3: 
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto')
            return True
        else:
            print(f'Opción invalida: {opcion}')
        return False # Cualquier opción que se ejecute que no sea la 5 no significará salir del sistema.
    

    def comprar_snack(self):
        id_snack = int(input('Seleccione el producto')) # creamos una variable id_snack donde almacenaremos la opción seleccionada por el cliente, el cual introducirá el número por pantalla, a través de un input
        snacks = self.servicio_snacks.get_snacks() # creamos una variable snacks y en ella traemos de vuelta todos los snacks con el método get_snacks que está en la clase servicios_snacks
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None) # Utilizamos el método next para iterar los siguientes elementos, en esta expresión podemos la lista que queremos iterar y el elemento.
                                        #filtrammos:  si el id del snack es igual al que está buscando el usuario a través de la función next() recuperamos el siguiente valor del iterador.
                                        # en caso de que no se encuentre este elemento devolvemos el valor de None.
                                        # Todo esto lo almacenamos en la variable snack
        if snack:
            self.productos.append(snack)  # Si el snack seleccionado existe, lo añadimos a nuestra lista de productos e imprimimos el mensaje.
            print(f'Snack encontrado {snack}')   
        else:
            print(f'Id del snack no encontrado: {id_snack}')  # Si no lo encuentra imprimimos esto.                         


    def mostrar_ticket(self):
        if not self.productos: # Si no tenemos nada en nuestra lista de productos imprimimos este mensaje:
            print('Lista vacia')
            return
        total = sum(snack.precio for snack in self.productos) # creamos la variable total, donde se van a iterar todos los productos seleccionados y se van a sumar sus precios.
        print('---Ticket de venta---')
        for producto in self.productos: # Iteramos cada uno de los productos:
            print(f'\t- {producto.nombre} - ${producto.precio: .2f} ') #formato precio de 2 decimales
        print(f'\tTotal -> ${total: .2f}') # fuera del ciclo for imprimimos el total

    
    def agregar_snack(self): # Método para agregar un snack al inventario
        nombre = input('Introduce el nombre del snack:') # Le pedimos a través de un input que introduzca el nombre
        precio = float(input('Introduce el precio del snack: ')) # Le pedimos que introduzca el precio del snack
        nuevo_snack = Snack(nombre, precio) #creamos el nuevo snack, para agregarlo a nuestro inventario
        self.servicio_snacks.agregar_snack(nuevo_snack)  #agregamos a la lista el nuevo snack, a través del método agragar snack que se encuentra en la clase servicios
        print(f'Snack agregado correctamente.')

# programa principal
if __name__ == '__main__': #Si el nombre es igual a main (comprobamos que estamos ejecutando este codigo desde este archivo)
    maquina_snacks = MaquinaSnacks() # creamos una variable maquina_snacks donde se almacene una estancia de clase de maquinasnacks
    maquina_snacks.maquina_snacks() # A partir de este objeto se llama al método maquina de snacks que pone en funcionamiento todo el programa