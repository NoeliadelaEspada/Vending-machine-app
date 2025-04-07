                        # snack
# Creamos la clase
class Snack:
    contador_snacks = 0   # Añadimos una variable de clase

    def __init__(self, nombre='', precio=0.0):  # Creamos el método constructor, con la variable nombre en blanco (ya que será personalizable) y precio en 0.
        Snack.contador_snacks += 1 # Primero incrementamos el contador en 1
        self.id_snack = Snack.contador_snacks # Usamos esta variable de contador para inicializar cada uno de los objetos que se vayan creando.
                                                # Accediendo a la variable de clase, que ya está incrementada.
        self.nombre = nombre # creamos el atributo de nombre y lo inicializamos.
        self.precio = precio # creamos el atributo de precio y lo inicializamos.

    def __str__(self): # añadimos el método str, que devolverá los datos id del snack, nombre y precio:
        return (f'Snack: id_snack = {self.id_snack}, nombre = {self.nombre}, '
        f'precio = {self.precio}')
    
    def escribir_snack(self): #Método para escribir la información anterior sin formato
       return f'{self.id_snack}, {self.nombre}, {self.precio}'