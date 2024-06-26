# Enunciado Original

## Problema 1

Desarrollar una función para encontrar las raíces de la ecuación cuadrática:
$$ax^2 + bx + c = 0$$

Ejemplo:

$2x^2 -10x + 5 = 0$

$x_1 = 4.4364$ $x_2 = 0.5635$

## Problema 2

Codificar un programa que permita capturar una frase, esta frase se pasará a una
función como parámetro. Esta función devolverá la cantidad de vocales y consonantes
de la frase.

Ejemplo:
```
Frase = "Divide y vencerás"
Cantidad de vocales = 7     # debería ser 6
Cantidad de consonantes = 8 # debería ser 9
```

## Problema 3

Implementar una función que devuelva la sumatoria de los cuadrados de N valores
aleatorios comprendidos entre 100.00 y 250.99. Muestre el resultado final en
notación científica.

## Problema 4

Dado un conjunto de palabras con los siguientes separadores `, . : -` se requiere
crear una función que obtenga como salida la cantidad de palabras de la frase.

Ejemplo:
```
Cadena = "Japón, China NorCorea-Italia: Rusia; EEUU.Inglaterra-Brasil"
Contar = 8
```

Lógica: Reemplazar todos los separadores por uno de ellos de tal forma que exista
un solo separador luego de cada palabra. Luego contar los separadores de la frase.
Finalmente, la cantidad de palabras será la cantidad de separadores +1.

Nota: Se sugiere utilizar las siguientes funciones: replace, count

## Problema 5

Crear una función llamada "Combinatorio" que invoque una función denominada "Factorial"
para calcular el numero combinatorio dado por:
$$C_{m}^{n}=\frac{m!}{n!(m-n)!}$$

Recuerde que el símbolo `!` representa el factorial de un número.

## Problema 6

Desarrolle un programa y la función correspondiente para calcular:
$$y=\frac{1-\sin(\frac{\pi}{4})\cos(\pi)^4}{1+\cos(\pi)^2}$$

Exprese el resultado con 4 decimales.

## Problema 7

Implemente una función para convertir coordenadas polares a rectangulares.
Debe tener en cuenta lo siguiente:

$x=r\cos{\theta}$

$y=r\sin{\theta}$

Recuerde que es un ánuglo y debe expresarlo en radianes.

## Problema 8

Desarrolle un programa Python, haciendo uso de una función para determinar el
resultado de la siguiente serie:
$$\frac{1}{2}-\frac{2}{2^2}+\frac{3}{2^3}-\cdots+\frac{n}{2^n}$$

Sugerencia: Use la función `math.pow()` para generar los denominadores

## Problema 9

Crear funciones que permitan realizar los siguientes tipos de cambio monetario a
Bolivianos:
- De Euro a Bs.
- De Dólar EE.UU a Bs.
- De Yen a Bs.
- De Libra Esterlina a Bs.

## Problema 10

Crear funciones que permitan obtener el área y perímetro de las siguientes figuras:
- Círculo $A=\pi r^2$, $P= 2\pi r$
- Paralelogramo $A =bh$, $P = 2(a+b)$
- Trapecio $A = (a+b)h/2$, $P = a + b + 2c$
- Rombo $A=(d_1d_2)/2$, $P = 4a$

---

> __**NOTA**__: El enunciado original contenía varios errores ortográficos
> que fueron corregidos.
