# ==============================================================================================
# 3. Pedidos en Pizzería(Parte 3)
# Modifica el programa de la Parte 2 agregando lo siguiente:
# pizzas | infantil | mediana | grande | gigante | morbida |
# mexicana | 50 | 160 | 260 | 370 | 480 |
# peperoni | 50 | 160 | 260 | 370 | 480 |
# hawaiana | 50 | 160 | 280 | 370 | 480 |
# especial | 57 | 190 | 260 | 390 | 520 |
# campirana | 50 | 180 | 280 | 370 | 480 |
# festiva | 50 | 180 | 280 | 370 | 480 |
# Con base a la tabla de precios modifica el programa para que se muestren los precios al
# seleccionar el tamaño de pizza y que en el resumen final se muestre la cuenta por pizza
# y por total.
# ----------------------------------------------------------------------------------------------
import os
ORDER = {}
ORDER_LINE = 0
ORDER_OPEN = True
ORDER_PIZZA = ""
ORDER_SIZE = ""
ORDER_QTY = 0

PIZZA_PRICE = {
    "mexicana": [50, 160, 260, 370, 480],
    "peperoni": [50, 160, 260, 370, 480],
    "hawaiana": [50, 160, 280, 370, 480],
    "especial": [57, 190, 260, 390, 520],
    "campirana": [50, 180, 280, 370, 480],
    "festival": [50, 180, 280, 370, 480]
}

PIZZA_SIZE = {
    "infantil": 0,
    "mediana": 1,
    "grande": 2,
    "gigante": 3,
    "morbida": 4
}


def clear_screen():
    '''Limpia la pantalla'''
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    """Imprime el mensaje de bienvenida"""
    print("="*80)
    print('\nBienvenidos a la pizzeria \"El Triangulo, Redondo en Caja Cuadrada\".\n')
    print("="*35+" M E N U "+"="*35)
    print("")
    print("Nuestro Menu")
    print("")
    print("Pizza\t\tInfantil\tMediana\t\tGrande\t\tGigante\t\tMorbida")
    for pizza, prices in PIZZA_PRICE.items():
        print(f"{pizza}\t{prices[0]}\t\t{prices[1]}\t\t{
              prices[2]}\t\t{prices[3]}\t\t{prices[4]}")
    print("")
    print("")


def print_line():
    '''Print Line Summary'''
    print(f"""Linea: {
        ORDER_LINE} - Cant: {ORDER_QTY} - Pizza: {ORDER_PIZZA} - Tamaño: {ORDER_SIZE}""")


def take_order():

    global ORDER_LINE, ORDER_PIZZA, ORDER_SIZE, ORDER_QTY
    ORDER_LINE += 1
    ORDER_PIZZA = input("Ingresa tu tipo de Pizza: ")
    ORDER_SIZE = input("Ingresa El tamaño que deseas: ")
    ORDER_QTY = input("Ingresa la cantidad: ")


def one_loop():
    clear_screen()
    welcome()
    take_order()
    print_line()


# La primera vuelta
one_loop()

while ORDER_OPEN:
    add_line = input("Agregar otra pizza? s/n: ")
    if add_line == "s":
        one_loop()
    else:
        ORDER_OPEN = False
print("")
print(f"Orden cerrada = total de lineas: {ORDER_LINE}")
