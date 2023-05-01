# SimpleEuler-Python

La clase **SimpleEuler** implementa el método de Euler para resolver ecuaciones diferenciales ordinarias de primer orden. El método de Euler es uno de los métodos numéricos más simples para resolver ecuaciones diferenciales, pero a menudo se utiliza como un primer paso para resolver ecuaciones más complejas.

## Requisitos

Para utilizar la clase **SimpleEuler** es necesario tener Python 3.x y la biblioteca **decimal** instalada. La biblioteca **math** viene incluida con Python por defecto.
```
pip install decimal
```

## Uso
Para utilizar la clase SimpleEuler simplemente crea una instancia de la clase y proporciona los parámetros necesarios:
```Python
from SimpleEuler import SimpleEuler

# Example: y'= 4x-2y;  y(0)=2;  y(0.5);  h= 0.1

equation = "4^x-2^y"
x0 = "0"
y0 = "2"
domain = "0.5"
h = "0.1"

example = SimpleEuler(equation, x0, y0, domain, h)

print(example.getListXY())
```

# Documentación
### Parametros
+ **equation** (str): la ecuación a resolver. 
    + Debe estar escrita en términos de x e y
    + Puede contener funciones matemáticas como raiz(y) o y^2 
    + sin, cos y etc no soportadas aún
+ **x0** (str): valor de x0.
+ **y0** (str): valor de y0.
+ **domain** (str): valor final de x para el que se desea resolver la ecuación.
+ **h** (str): el tamaño del paso.

### Métodos
+ **getAll()**: Devuelve un diccionario que contiene todas las listas de valores de x, y, f, así como los parámetros de entrada equation, x0, y0, domain y h.

+ **getListX()**: Devuelve una lista de los valores de x.

+ **getListY()**: Devuelve una lista de los valores de y.

+ **getListXY()**: Devuelve un diccionario con dos listas: una lista de los valores de x y otra lista de los valores de y.

+ **getDomain()**: Devuelve el valor final de x para el que se desea resolver la ecuación.

+ **getEquation()**: Devuelve la ecuación a resolver.

+ **getX0()**: Devuelve el valor inicial de x.

+ **getY0()**: Devuelve el valor inicial de y.

+ **getH()**: Devuelve el tamaño del paso.

+ **getF()**: Devuelve una lista de los valores de f.



