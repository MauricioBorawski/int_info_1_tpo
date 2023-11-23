# TPO Grupo 8

## Integrantes:

- Araujo Nicolas Ezequiel
- Borawski Mauricio Nicolas
- Chaves Santiago Jesus
-  Perg Schneider Santiago
- Racchi Agustin Tomas

## Tabla de contenido
1. Presentacion del proyecto
2. Estructura
3. Consigna 1
4. Consigna 2
5. Consigna 3
6. Consigna 4

---
# Presentacion del Proyecto

Un club local de una ciudad, tiene diversas actividades deportivas y culturales que ofrece a sus socios.
Además, por la antigüedad o por la edad, hay diferentes categorías de tipos de socios que esta institución posee.
Todos los meses, tienen que generar la facturación del socio del mes, el cual se calcula según la cantidad de actividades y el tipo de socio que es.

## Datos

| Tipo de Socio  | Costo Cuota Social  | Hasta 2 Act  |  3 o mas Act  |
|---|---|---|---|
| Junior  | $750  | $1500  | $1000  |
| Standar  | $3000  | $2500  | $1500  |
| Platino  | $2300  | $1500  | $1300  |
| Oro | $300 | $1500 | $1300 |
| Vitalicio | $0 | $1000 | $750 |

## Consignas

1. Total de la facturación del mes y cuántos socios hay.
2. Total de facturación por tipo de socio y la cantidad de actividades ordenado por facturación.
3. Listado completo detallado del total facturado de cada socio con su tipo, ordenado por el total facturado.
4. Poder seleccionar un tipo de socio y que se detallen la facturación y cantidad de actividades de cada uno.

---

## Aclaraciones

1. La cantidad de socios varia entre `100` como minimo y un maximo de `100`

2. La cantidad de actividades que cada socio puede hacer es de un maximo de 6 y un minimo de 0.

# Estructura del Proyecto

El programa consiste en:

- Constantes
- Metodos Generales
- Funciones Principales
- Programa Principal

---

# Constantes

## MENU

Es una lista de `strings` que contiene todas las opciones que puede ejecutar el programa.

## TIPO_SOCIO

Es una lista de `strings` que contiene cada tipo de socio, su uso principal era la de poder mostrar al usuario el tipo de socio mas claramente.

## CANTIDAD DE ACTIVIDADES

Es una lista de `strings` que sirve para mostrar la cantidad de actividades.

## COSTOS

Es una lista anidada que contiene `intergers` que representan los costos dependiendo de su cantidad de actividades y estan ordenados por tipo de socio.

---

# Metodos Generales

## mostrar_menu
Se encarga de mostrar en pantalla el menu principal con el que el usuario interactua.

Recive como parametros las `opciones` a mostrar en pantalla.

## generar_factura
Se encarga de calcular los costos por cantidad de actividad del socio.

Recive como parametro el `tipo_socio` y la `cant_actividades`

## generar_socios

Se encarga de generar una lista anidada con la informacion de cada socio, indicando un `id` unico, el `tipo_socio`, la `cant_actividades` y su `facturacion`.

Recive como parametro un numero `minimo` y `maximo`

```python
[
id, Platino, actividades, 3900
[0, 2, 3, 4500],
]
```

---
## ordenar_matriz

Se encarga de odernar una lista segun una clave indicada en orden descendente.

Recive como parametro la `lista` y una `clave`

## vec_ord_vec
Se encarga de ordenar una lista por su facturacion en orden descendente.

Recive como parametro la `lista` a ordenar.

## crear_arreglo_con_0

Se encarga de generar una lista anidada y les inserta 0 segun las filas y columnas ingresadas a la funcion.

Recive como parametros la cantidad de `filas` y de `columnas`

## manejar_opciones

Se encarga manejar el input del usuario y llamar a la funcion que corresponda.

Recive como parametros una `opcion` y la lista de `socios`

---

# Programa Principal

Se encarga de generar el listado de `socios` y de llamar a las funciones necesarias para que funcione el programa.

---

# Consigna 1

### Total de la facturación del mes y cantidad de socios

---

# Consigna 2

### Total de facturación por tipo de socio y la cantidad de actividades, ordenado por facturacion

---

# Consigna 3

### Listado completo detallado del total facturado de cada socio con su tipo, ordenado por el total facturado

---

# Consigna 4

### Poder seleccionar un tipo de socio y que se detallen la facturación y cantidad de actividades de cada uno.  




