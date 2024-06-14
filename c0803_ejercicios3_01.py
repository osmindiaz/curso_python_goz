# ===============================================================================================================
# 1. Pedidos en Pizzería (Parte 1)
# Escribe un programa que le permita al usuario pedir una pizza.
# Requerimientos:
# - Al inicio el programa saluda al usuario ***
# - El programa muestra el mensaje “Selecciona una pizza” y muestra las siguientes pizzas:
# mexicana, peperoni, hawaiana, especial, campirana, festiva.
# - El usuario selecciona su pizza
# - El programa muestra el mensaje “Selecciona el tamaño de tu pizza” y muesta las siguientes opciones:
# infantil, mediana, grande, gigante, morbida
# - El usuario selecciona el tamaño
# - El programa pide al usuario que escriba la dirección de su domicilio.
# - El programa pide al usuario que escriba su número de teléfono.
# - El programa muestra un resumen de todo el pedido.
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


pizza_type = ["mexicana", "peperoni", "hawaiana",
              "especial", "campirana", "festiva"]
pizza_size = ["infantil", "mediana", "grande", "gigante", "morbida"]

clear_screen()
welcome()
customer_name = input("Por favor Ingresa tu nombre: ")


clear_screen()
welcome()
phone = input("Por favor Ingresa tu Numero de Telefono: ")


clear_screen()
welcome()
print("-"*7 + " " + "Estos son nuestros Tipos de Pizza"+" "+"-"*10)
for pizza in pizza_type:
    print(f"\t- {pizza}")
pizza_type = input("Escribe tu seleccion de Tipo de Pizza: ")


clear_screen()
welcome()
print("-"*7 + " " + "Estos son nuestros Tamaños de Pizza"+" "+"-"*10)
for size in pizza_size:
    print(f"\t - {size}")
pizza_size = input("Escribe tu seleccion de Tamaño de Pizza: ")


clear_screen()
welcome()
print("Ingresa la direccion para enviar tu triangulo redondo en una caja cuadrada\n")
address = input(": ")


clear_screen()
welcome()
print(f"""Resumen de tu pedido:\n\n\tCliente: {customer_name}\n\tDireccion: {address}\n\tTe enviaremos una pizza \'{
      pizza_type}\' - {pizza_size}\n\tA: {address}\n\n\tSi no podemos localizarte te vamos a marcar al numero {phone}\n\n\'""")


# for country, country_info in countries.items():
#    print(f"\n el pais es: {country}")
#    print(f"su capital es: {country_info['capital']}")
#    print(f"su comida es: {country_info['comida']}")
