## Introducción
s
### Como funciona Python
Hay lenguajes que son interpretados y otros compilados
**Compilado:** convierte el código a binarios que lee el sistema operativo.
**Interpretado:** requieren de un programa que lea la instrucción del código en tiempo real, y la ejecute. Tiene un paso intermedio, la maquina virtual que se puede ejecutar en diferentes sistemas operativos. *python*
**Intermedio:** se complila el código fuente a un lenguaje intermedio y este último se ejecuta en una máquina virtual.

**Garbage collector (recolector de basura):** toma los objetos y variables que no están en uso y los elimina.

**__pycache__** en esta carpeta esta el *bytecode*, el código intermedio, que crea python para que lo pueda leer la máquina virtual.

### Organiza los archivos de tus proyectos
**Paquetes:** es un conjunto de módulos. Carpetas que contienen módulos. __init__.py
**Módulos:** es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar. *.py*

### ¿Qué son los 'tipados'?
## Static Typing
Hay cuatro clasificaciones según el tipado: estático, dinámico, débil y fuerte.

*El tipado del lenguaje depende de cómo este trata los tipos de datos.* El tiempo de ejecución es el tiempo en el que podemos ver a nuestro programa funcionar.

* **Static:** levantan los errores de tipo en tiempo de compilación. Por ejemplo *java*.
* **Dynamic:** no levantan el error en tiempo de compilación, sino en tiempo de ejecución. Por ejemplo *python*.
* **Strong:** tratan con más severidad a los datos de diferentes tipos.
* **Weak:** tratan con menos severidad a los datos de diferentes tipos.

## Tipado estático en Python
**a: int = 5** --> forma de asignar el tipo a las variables
**b: str = 'hola'**

Dentro de funciones podemos hacer 
def <nombre_func> ( <parametro1> : <tipo_de_dato>, <parametro2> : <tipo_de_dato> ) ->  <tipo_de_dato> :
	pass


Para listas y diccionarios
from typing import Dict, List, Tuple

positives: List [int] = [1,2,3,4,5]

users: Dict [str, int] = {
	"argentina": 1.
	"mexico": 34,
	"colombia": 45,
}

countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
	{
		"coord1": (1,2),
		"coord2": (3,5)
	},
	{
		"coord1": (0,1),
		"coord2": (2,5)
	}
]

El modulo **mypy** se complementa con el módulo **typing** ya que permitirá mostrar los errores de tipado debil en Python

## Scope: alcance de las variables
Una variable solo está disponible dentro de la región donde fue creada

### Local Scope
Es la región que corresponde al ambito de una función, donde podremos tener una o mas variables, las viriables van a ser accesibles únicamene en esta region y no serán visibles para otras regiones.

### Global scope
Estas podrán ser accesibles desde cualquier parte del código.

## Closures
Es una forma de acceder a bariables de otros scopes a través de una nested function.
### Nested funtions 
Son funciones anidadas
Puedo crear variables que tienen todo el contenido de la función, se pueden ejecutar usando parentesis.

**Reglas para encontrar un closure**
* Debemos tener una nested function
* La nested funtion debe referenciar un valor de un scope superior 
* La función que envuelve a la nested funtion debe retornarla también.

**Dónde aparecen los closures**
- Cuando en una clase solo tengo un metodo
- Cuanto se trabajan con decoradores

## Decoradores
Función que recibe como parámetro otra función, le añade cosas, y retorna una función diferente. Es un clasure.

**Azucar sintactica:** cuanto tenemos un codigo que esta embellecido para que nosotros lo veamos de una manera más estetica. 

## Iteradores
* **Iterables:** todos los objetos que podemso recorrer en un cilcio. Listas, string
* **Iteradores:** Ahorra recursos, puedo almacenar secuencias y progreciones matemáticas, ocupa poca memoria.  

El **ciclo for** hace los mismo que un while true. Osea el ciclo **for es azúcar sintática**
 

## Generadores
**Azúcar sintáctica** de los interadores. Son funciones que guardan un estado.

## Set
Es una colección desordenada de elementos únicos e inmutables

### Metodos
* **.add(elemento):** Añade un elemento al set
* **.update(elementos):** Añade varios elementos al set
* **.remove(elemento):** elimina un elemento del set
* **.pop():** elimina un elemento aleatorio del set
* **.clear():** eliminar todos los elementos del set

### Operaciones
* **Unión (|):** resultado de combinar todos los elementos de los dos conjuntos
* **Intersección (&):** resultado de quedarse con los elementos que tienen en comun los dos conjuntos
* **Diferencia (-):** resultado de tomar dos conjuntos y de uno quitar todos los elementos que tiene el otro
* **Diferencia simetrica (^):** Quedarse con los elementos que no comparten. Es lo contrario a la intersección.

## Zonas horarias
Se trabaja con el método **pytz**
