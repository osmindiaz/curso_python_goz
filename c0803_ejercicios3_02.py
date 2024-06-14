# ===============================================================================================================
# 2. Pedidos en Pizzería(Parte 2)
# Modifica el programa de la Parte 1 agregando lo siguiente:
# - El programa al final debe preguntar si el usuario quiére otra pizza
# - En caso afirmativo todo el programa vuelve a hacer las preguntas y el resumen del final
# debe mostrar toda la información del pedido.
# - Las preguntas de domicilio y teléfono sólo se pregunten una sola vez.
# ---------------------------------------------------------------------------------------------------------------
import os


def welcome():
    print("="*80)
    print('\nBienvenidos a la pizzeria \"El triangulo, Redondo en Caja Cuadrada\".\n')
    print("="*80)
    print("")


def clear_screen():
    # Verificar el sistema operativo y ejecutar el comando correspondiente
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux, macOS)
        os.system('clear')


def get_order_detail():
    clear_screen()
    welcome()
    print("-"*7 + " " + "Estos son nuestros Tipos de Pizza"+" "+"-"*10)
    for pizza in pizza_types:
        print(f"\t- {pizza}")
    pizza_type = input("Escribe tu seleccion de Tipo de Pizza: ")
    ordered_type.append(pizza_type)

    clear_screen()
    welcome()
    print("-"*7 + " " + "Estos son nuestros Tamaños de Pizza"+" "+"-"*10)
    for size in pizza_sizes:
        print(f"\t - {size}")
    pizza_size = input("Escribe tu seleccion de Tamaño de Pizza: ")
    ordered_size.append(pizza_size)


pizza_types = ["mexicana", "peperoni", "hawaiana",
               "especial", "campirana", "festiva"]
pizza_sizes = ["infantil", "mediana", "grande", "gigante", "morbida"]
ordered_type = []
ordered_size = []

clear_screen()
welcome()
customer_name = input("Por favor Ingresa tu nombre: ")


clear_screen()
welcome()
phone = input("Por favor Ingresa tu Numero de Telefono: ")

clear_screen()
welcome()
print("Ingresa la direccion para enviar tu triangulo redondo en una caja cuadrada\n")
address = input(": ")

# ------------------------------------------------------------------------- Inicio del loop
while True:
    clear_screen()
    welcome()
    get_order_detail()

    clear_screen()
    welcome()
    add_to_order = input(
        "Deseas agregar algo más a tu pedido? (si/no): ").strip().lower()
    if add_to_order != "si":
        break
# -------------------------------------------------------------------------Fin del loop
clear_screen()
welcome()
# Convertir Listas > Tuplas > Diccionarios
order_tuple = zip(ordered_type, ordered_size)
order_dict = dict(order_tuple)
# -------------------------------------------------------------------------Crear Reporte del pedido
print(f"""Resumen de tu pedido:\n\n\tCliente: {
      customer_name}\n\tDireccion: {address}\n\tTelefono:{phone}\n\n""")
for ptype, psize in order_dict.items():
    print(f'{ptype} - {psize}')
print("")
