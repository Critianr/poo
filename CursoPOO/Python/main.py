# En Python encontrarás un concepto denominado Métodos Mágicos, estos métodos son llamados automática y estrictamente bajo ciertas reglas. El método constructor en Python forma parte de esta familia de métodos y como aprendimos en la clase anterior lo declaramos usando __init__, aunque si nos ponemos estrictos este método no construye el objeto en sí. El encargado de hacer esto es __new__ y el método __init__ se encargará de personalizar la instanciación de la clase, esto significa que lo que esté dentro de __init__ será lo primero que se ejecute cuando se cree un objeto de esta clase.

# Para nuestro proyecto tenemos la necesidad de que algunas variables se inicialicen obligatoriamente cuando ocurra la instanciación. Así que declaremos el método __init__ en las clases de nuestro proyecto con las propiedades obligatorias.

# Para la clase Account quedaría algo así, notarás que usamos la palabra clave self, esta es muy parecida a lo que venimos trabajando a otros lenguajes con this. Y como su nombre lo dice hace referencia a los datos que componen la clase, en este caso self.name está llamando al atributo name que se encuentra en la línea 3 de la clase y, le está asignando el dato que se pasa en el método __init__ de la línea 8.

from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")
    car1 = Car('AMD123',Account('Carlos E', 'EQW123'))
    print(vars(car1))
    print(vars(car1.driver))
