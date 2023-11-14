from random import randint

# Constantes

MENU = ["Total de la facturación del mes y cantidad de socios",
        "Total de facturación por tipo de socio y la cantidad de actividades "
        "ordenado por facturación",
        "Listado completo detallado del total facturado de cada socio"
        "con su tipo, ordenado por el total facturado",
        "Seleccion de socio",
        "Salir",
        ]

TIPO_SOCIO = ["Junior", "Standard", "Platino", "Oro", "Vitalicio"]

CAT_CANT_ACT = ["0", "hasta 2", "mas de 3"]

COSTOS = [
    [750, 1500, 1000],
    [3000, 2500, 1500],
    [2300, 1500, 1300],
    [1900, 1500, 1300],
    [0, 1000, 750]
]

# Metodos generales


def mostrar_menu(options: []) -> None:
    contador = 1

    for opcion in options:
        print(contador, opcion)
        contador += 1


def generar_factura(tipo_socio, cant_activades):
    cuota_social = COSTOS[tipo_socio][0]
    valor_por_actividad = None

    if cant_activades >= 3:
        valor_por_actividad = 1
    else:
        valor_por_actividad = 2

    return cuota_social + (COSTOS[tipo_socio][valor_por_actividad] * cant_activades)


def generar_socios(min, max):
    socios = []
    cantidad_generar = randint(min, max)
    id_socio = 0

    for _ in range(cantidad_generar):
        socio = []
        tipo_socio = randint(0, 4)
        cant_actividades = randint(0, 6)
        facturacion = generar_factura(tipo_socio, cant_actividades)

        socio.append(id_socio)
        socio.append(tipo_socio)
        socio.append(cant_actividades)
        socio.append(facturacion)

        socios.append(socio)

        id_socio += 1

    return socios

#Ordena la matriz segun el campo cve indicado en orden descendente y la devuelve
def ordenar_matriz(matriz,cve): 
    for i in range (1, len(matriz)):
        aux = matriz[i]
        j = i
        while j > 0 and matriz[j-1][cve] < aux[cve]:
            matriz[j] = matriz[j-1]
            j = j - 1
        matriz[j] = aux
    return matriz


#Crea un vector auxiliar las posiciones del vector ordenados por facturacion en orden descendente y lo devuelve
def vec_ord_vec(vector): 
    vec = []
    #Le asigna el indice al vector
    for i in range (0, len(vector)):
        vec.append(i)
    #Comienza la funcion de ordenamiento por insercion
    for i in range (1, len(vector)):
        aux = vec[i]
        j = i
        while j > 0 and vector[vec[j-1]] < vector[aux]:
            vec[j] = vec[j-1]
            j = j - 1
        vec[j] = aux
    return vec


#Crea y devuelve un array relleno con 0's con la cantidad de filas y columnas pedidas
def crear_arreglo_con_0(filas,columnas): 
    matriz = []
    for f in range(filas):
        if columnas == (1):
            matriz.append(0)
        else:
            matriz.append([])
            for c in range(columnas):
                matriz[f].append(0)
    return matriz

# Consigna 1
def total_facturacion_mes(tipo_socio, cant_actividades) -> None:
    #Se inicializan los contadores de cantidad y tipos de socios
    cant_socios = 0
    junior = 0
    standard = 0
    platino = 0
    oro = 0
    vitalicio = 0
    #Se recorre la lista de tipos de socios para asignarle a cada uno su correspondiente factura
    for i in range(len(tipo_socio)):
        if tipo_socio[i] == 0:
            if cant_actividades[i] >= 0 and cant_actividades[i] <= 2:
                junior += (750 + (1500 * cant_actividades[i]))
            elif cant_actividades[i] >= 3 and cant_actividades[i] <= 6:
                junior += (750 + (1000 * cant_actividades[i]))
            #Se agrega un socio
            cant_socios += 1
        if tipo_socio[i] == 1:
            if cant_actividades[i] >= 0 and cant_actividades[i] <= 2:
                standard += (3000 + (2500 * cant_actividades[i]))
            elif cant_actividades[i] >= 3 and cant_actividades[i] <= 6:
                standard += (3000 + (1500 * cant_actividades[i]))
            #Se agrega un socio
            cant_socios += 1
        if tipo_socio[i] == 2:
            if cant_actividades[i] >= 0 and cant_actividades[i] <= 2:
                platino += (2300 + (1500 * cant_actividades[i]))
            elif cant_actividades[i] >= 3 and cant_actividades[i] <= 6:
                platino += (2300 + (1300 * cant_actividades[i]))
            #Se agrega un socio
            cant_socios += 1
        if tipo_socio[i] == 3:
            if cant_actividades[i] >= 0 and cant_actividades[i] <= 2:
                oro += (1900 + (1500 * cant_actividades[i]))
            elif cant_actividades[i] >= 3 and cant_actividades[i] <= 6:
                oro += (1900 + (1300 * cant_actividades[i]))
            #Se agrega un socio
            cant_socios += 1
        if tipo_socio[i] == 4:
            if cant_actividades[i] >= 0 and cant_actividades[i] <= 2:
                vitalicio += (0 + (1000 * cant_actividades[i]))
            elif cant_actividades[i] >= 3 and cant_actividades[i] <= 6:
                vitalicio += (0 + (750 * cant_actividades[i]))
            #Se agrega un socio
            cant_socios += 1
        #Se suman todas las facturas de todos los tipos de socios
        facturacion_total = junior + standard + platino + oro + vitalicio
        #Se devuelve el total facturado y la cantidad de socios
        return facturacion_total, cant_socios

    return None

# Consigna 2

def calcular_fac_tot_por_tipo_socio(matriz):
    #Se crean las matrices acumuladoras inicializadas en 0
    fact_por_act = crear_arreglo_con_0(5,3)
    fact_tot_tipo = crear_arreglo_con_0(5,1)
    #Se comienza el ciclo en el cual se recorre la matriz sumando los facturados
    for i in range(len(matriz)):
        #Se crea una variable catalogo que sirve para ver si el socio entra en la categoria
        #de 0 actividades, hasta 2 actividades o 3 o mas actividades
        cat_act = 0
        if 0 < matriz[i][2] <= 2:
            cat_act = 1
        elif matriz[i][2] > 2:
            cat_act = 2
        #Se realizan las sumas en las matrices acumuladoras
        fact_por_act[matriz[i][1]][cat_act] += matriz[i][3]
        fact_tot_tipo[matriz[i][1]] += matriz[i][3]
    #Se crea un vector orden segun el total facturado de mayor a menor
    orden_tot = vec_ord_vec(fact_tot_tipo)
    #Se recorre el vector de facturados totales por tipo de socio imprimiendo los tipos de socios
    for i in range(len(fact_tot_tipo)):
        print("Socios ",TIPO_SOCIO[orden_tot[i]],":",sep = "")
        #Se crea un vector orden segun el facturado por cantidad de actividades de mayor a menor
        orden_act = vec_ord_vec(fact_por_act[orden_tot[i]])
        #Se recorre el vector correspondiente a ese tipo de socio de la matriz facturado por cant de actividades
        for j in range(len(fact_por_act[orden_tot[i]])):
            print("Con",CAT_CANT_ACT[orden_act[j]],"actividades:", fact_por_act[orden_tot[i]][orden_act[j]])
        print() #Imprime un espacio para separar los tipos de socios
        

# Consigna 3
def listado_detallado_socios(socios: []) -> None:
    socios_ordenados = ordenar_matriz(socios, 3)  # Ordena la matriz por el total facturado

    for socio in socios_ordenados:
        id_socio = socio[0]
        tipo_socio = TIPO_SOCIO[socio[1]]
        total_facturado = socio[3]

        print("El socio", id_socio, ": Tipo" , tipo_socio , ", debe abonar un total de :" , total_facturado, "pesos")
        
    return None

# Consigna 4


def detalle_socio_por_tipo(socios: []) -> None:
    print("Seleccione el tipo de socio: ")
    mostrar_menu(TIPO_SOCIO)
    option_socio = 0
    
    while option_socio > 5 or option_socio < 1:
        option_socio = int(input("\nIngrese una opción válida: "))
    
    for socio in socios:
        if socio[1] == option_socio-1:
            print("El socio numero", socio[0], "pertenece al tipo", TIPO_SOCIO[option_socio-1], ", realiza", socio[2], "actividades y debe abonar", socio[3], "pesos.")
    return main



def manejar_opciones(opcion, socios) -> None:
    print("\n")

    if opcion == 1:
        total_facturacion_mes(socios)
    elif opcion == 2:
        calcular_fac_tot_por_tipo_socio(socios)
    elif opcion == 3:
        listado_detallado_socios(socios)
    elif opcion == 4:
        detalle_socio_por_tipo(socios)
    elif opcion == 5:
        print("Gracias por usar el programa")
    else:
        print("Opción incorrecta")

# Funcion principal


def main() -> None:
    socios = generar_socios(100, 1000)
    option = None


    while option != 5:
        print("\n")
        mostrar_menu(MENU)
        option = int(input("Ingrese una opción: "))
        manejar_opciones(option, socios)


main()
