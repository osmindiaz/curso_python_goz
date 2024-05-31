# ===================================================================================================================================================================
# 1.Calculadora de IVA - El programa al iniciar debe presentar un mensaje de saludo y solicitarle al usuario que escriba una cantidad de dinero.
# El programa deberá calcular el 16% de esa cantidad y presentar como resultados: Tus resultados son:
# IVA al 16%: / La cantidad sin IVA: / La cantidad con IVA: / Qué divertido es pagar impuestos!
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from decimal import *

# getcontext().prec = 8

# print("="*50)
# print("")
# print("Bienvenido contribuyente a la calculadora de IVA")
# print("")
# subtotal = Decimal(input("Escribe la cantidad del subtotal: "))
# iva = Decimal('0.16')*Decimal(subtotal)
# total = Decimal(subtotal)+iva
# print("")
# print(f"Subtotal (Cantidad sin IVA pues): $ {subtotal:,.2f}")
# print(f"IVA (lo que te chinga el SAT): $ {iva:,.2f}")
# print(f"Total (Lo que vas a pagar por todo bru): $ {total:,.2f}")
# print("")
# print("Que divertido es pagar impuestos ~.~! ")
# print("")
# print("="*50)


# ===================================================================================================================================================================
# 2. Calculadora de IVA (2)
# El programa es una variante de la calculadora de iva original pero en esta ocasión el programa permite
# que el usuario también pueda decir cuanto equivale el iva (con numero decimal).
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from decimal import *
# print("")
# print("="*80)
# print("Calculadora de Impuestos")
# print("="*80)
# print("")
# print("")
# print("Que deseas calcular?")
# print("")
# print("")
# selector_01 = input("El IVA en base al Subtotal? (\'Si\' / \'No\'): ")

# if selector_01 == "Si":
#    subtotal = Decimal(input("Ingresa el Subtotal: "))
#    iva = (Decimal(subtotal)*Decimal(.16))
#    total = Decimal(subtotal)+Decimal(iva)
#    print("")
#    print(f"Subtotal: {subtotal:,.2f}  *")
#    print(f"IVA: {iva:,.2f}")
#    print(f"Total: {total:,.2f}")
#    print("")
#    print("Que gacho es pagar impuestos :\'(")
#    print("")
#    print("_"*80)
#    print("")

# else:
#    selector_02 = input("El IVA en base al Total? (\'Si\' / \'No\'): ")
#    if selector_02 == "Si":
#        total = Decimal(input("Ingresa el Total: "))
#        subtotal = (Decimal(total)/Decimal(1.16))
#        iva = (Decimal(total)-Decimal(subtotal))
#        print("")
#        print(f"Subtotal: {subtotal:,.2f}")
#        print(f"IVA: {iva:,.2f}")
#        print(f"Total: {total:,.2f}  *")
#        print("")
#        print("Que gacho es pagar impuestos :\'(")
#        print("")
#        print("_"*80)
#        print("")

#    else:
#        selector_03 = input("El Total en base al IVA? (\'Si\' / \'No\'): ")
#        if selector_03 == "Si":
#            iva = Decimal(input("Ingresa el IVA: "))
#            subtotal = (Decimal(iva)/Decimal(.16))
#            total = (Decimal(subtotal)+Decimal(iva))
#            print("")
#            print(f"Subtotal: {subtotal:,.2f}")
#            print(f"IVA: {iva:,.2f}  *")
#            print(f"Total: {total:,.2f}")
#            print("")
#            print("Que gacho es pagar impuestos :\'(")
#            print("")
#            print("_"*80)
#            print("")
#        else:
#            print("")
#            print("")
#            print("No seleccionaste nada, que pedo contigo, pos quien te entiende!")
#            print("")
#            print("")


# ===================================================================================================================================================================
# 3. Generador de cuentos El programa al iniciar debe presentar un mensaje de saludo, posteriormente comenzará a preguntarle al
# usuario lo siguiente: el nombre del usuario, edad, lugar, animal, país, comida, color, profesión, parte del cuerpo.
# La salida del programa debe ser un cuento con la siguiente estructura:
# A sus edad años nombre se fue de viaje a país. Su trabajo de profesión le permitió
# visitar este lejano lugar en el que pudo comer comida. Lamentablemente terminó visitando
# al doctor ya que su parte del cuerpo se hinchó y se puso de color color por estar jugando con un/una
# animal que casualmente encontró en un lugar
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("")
# print("="*80)
# print("")
# print(("Bienvenido(A) al \'cuenta cuentos 3000\', por favor ingresa los siguientes datos").upper())
# print("")
# print("="*80)
# print("")

# name = input("Ingresa un nombre: ")
# age = input("Ingresa una edad: ")
# country = input("Ingresa un pais: ")
# place = input("Ingresa un lugar: ")
# animal = input("Ingresa un animal: ")
# food = input("ingresa una comida: ")
# profession = input("Ingresa una profession: ")
# bodypart = input("Ingresa una parte del cuerpo: ")
# color = input("Ingresa un color: ")

# print(f"""
# A sus {age} años {name} se fue de viaje a {country}. Su trabajo de {profession} le permitió
# visitar este lejano lugar en el que pudo comer {food}. Lamentablemente terminó visitando
# al doctor ya que su {bodypart} se hinchó y se puso de color {color} por estar jugando
# con un/una {animal} que casualmente encontró en un {place}
#
#                                                                                [fin..]
# """)


# ===================================================================================================================================================================
# 4. Generador de nombre de boxeador o boxeadora
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente pedirá el primer apellido
# del usuario. El sistema generará un nombre de boxeador o boxeadora sacando un elemento aleatorio de
# una lista y concatenandolo con el apellido de la persona.

# ['El mantequilla ', 'El guapo ', 'El seboso ', 'El gorgojo ', 'El cepillo ', 'El otaku ', 'El ratón ', 'El
# maravilla ', 'El manatí ','El sabroso ', 'El pollo ', 'El gallo', 'El salsita', 'El ardilla ', 'El fantastico ',
# 'El hermoso ', 'El sudado', 'El fornido']

# ['La mantequilla ', 'La guapa ', 'La sebosa ', 'La gorgojita ', 'La llamarada ', 'La tepiteña ', 'La
# ratoncita ', 'La pantera ', 'La sonrisas ','La florecita ', 'La espartana ', 'La reina', 'La ruda', 'La
# pegalona ', 'La fantástica ', 'La hermosa ', 'La sudada', 'La fornida']
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("")
# print("="*80)
# print("")
# print("=======================  COMISION INTERNACIONAL DE BOXEO ========================")
# print("")
# print("Asi que eres una persona muy ruda eh! \v\t\t\t\tTe pondremos un nombre profesional")
# print("")
# print("="*80)
# print("")
# name = input("Ingresa tu Nombre: ")
# lastname = input("Ingresa tu Apellido: ")
# gender = input("Ingresa tu Genero \'Masculino\', \'Femenino\',\'Otro\': ")
# gender = gender.lower()
# ## Aqui creo las listas
# rudos = ['El mantequilla', 'El guapo', 'El seboso', 'El gorgojo', 'El cepillo', 'El otaku', 'El ratón', 'El maravilla', 'El manatí',
#         'El sabroso', 'El pollo', 'El gallo', 'El salsita', 'El ardilla', 'El fantastico', 'El hermoso', 'El sudado', 'El fornido']
# rudas = ['La mantequilla', 'La guapa', 'La sebosa', 'La gorgojita', 'La llamarada', 'La tepiteña', 'La ratoncita', 'La pantera',
#         'La sonrisas', 'La florecita', 'La espartana', 'La reina', 'La ruda', 'La pegalona', 'La fantástica', 'La hermosa', 'La sudada', 'La fornida']
# otros = rudos+rudas
# ## Aqui las convierto en conjuntos para que se ordenen aleatoriamente
# rudos = set(rudos)
# rudas = set(rudas)
# otros = set(otros)
# ## Aqui las paso a listas otra vez para poderlas llamar a mi f-string
# rudos = list(rudos)
# rudas = list(rudas)
# otros = list(otros)

# if gender == "masculino":
#    print("")
#    print("")
#    print("-"*80)
#    print(f"Desde ahora seras conocido como: {
#          name} \"{rudos[-1]}\" {lastname}")
#    print("-"*80)
#    print("")
#    print("")
# else:
#    if gender == "femenino":
#        print("")
#        print("")
#        print("-"*80)
#        print(f"Desde ahora seras conocida como: {
#              name} \"{rudas[-1]}\" {lastname}")
#        print("-"*80)
#        print("")
#        print("")
#    else:
#        if gender == "otro":
#            print("")
#            print("")
#            print("-"*80)
#            print(f"Desde ahora te llamarán: {
#                  name} \"{otros[-1]}\" {lastname}")
#            print("-"*80)
#            print("")
#            print("")
#        else:
#            print("")
#            print("")
#            print("-"*80)
#            print("Y tú; Eres marciano o qué?!")
#            print("-"*80)
#            print("")
#            print("")


# ===================================================================================================================================================================
# 5. Generador de cuentos (2)
# Programa un generador de cuentos como el del ejercicio tres pero esta vez crea los cuentos
# de manera aleatorio por medio de listados creados por ti.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("")
# print("="*80)
# print("")
# print(("Bienvenido(A) al \'cuenta cuentos 3000 PRO ULTRA\', por favor ingresa los siguientes datos").upper())
# print("")
# print("="*80)
# print("")

# name = ["Alejandro", "Beatriz", "Carlos", "Dolores", "Elena", "Francisco", "Gabriela", "Hernán", "Isabel", "Javier", "Karla", "Luis", "María",
#        "Natalia", "Óscar", "Patricia", "Quintín", "Raquel", "Santiago", "Teresa", "Ulises", "Valeria", "Wilfredo", "Ximena", "Yolanda", "Zacarías"]

# age = [61, 64, 38, 17, 73, 59, 27, 37, 47, 16, 56, 41, 26, 60, 48, 53, 32, 18, 52, 57, 50, 36, 62, 55, 42, 21, 25, 67, 58, 44,
#       39, 29, 46, 54, 33, 71, 28, 65, 66, 49, 23, 24, 31, 72, 43, 69, 20, 68, 74, 30, 45, 63, 34, 75, 51, 40, 22, 35, 15, 70, 19]

# country = ["Argentina", "Brasil", "Chile", "Colombia", "México", "Perú", "Venezuela", "Uruguay", "Paraguay", "Bolivia", "Ecuador", "Guatemala", "Honduras", "El Salvador", "Nicaragua", "Costa Rica", "Panamá", "Cuba", "República Dominicana", "Puerto Rico", "España", "Portugal", "Francia", "Italia", "Alemania",
#           "Reino Unido", "Países Bajos", "Bélgica", "Suiza", "Austria", "Suecia", "Noruega", "Dinamarca", "Finlandia", "Islandia", "Rusia", "China", "Japón", "Corea del Sur", "India", "Australia", "Nueva Zelanda", "Sudáfrica", "Egipto", "Marruecos", "Nigeria", "Kenya", "Turquía", "Israel", "Arabia Saudita"]

# place = ["cocina", "recámara", "baño", "sala", "comedor", "sótano", "ático", "garaje", "pasillo", "jardín trasero", "parque", "biblioteca", "restaurante", "cine", "escuela", "supermercado", "hospital", "estación de policía", "bomberos", "gimnasio", "el espacio", "Marte", "la cima de un volcán", "el fondo del océano", "un desierto", "el Triángulo de las Bermudas", "una isla desierta", "la Luna", "el Polo Norte", "el Amazonas",
#         "dentro del ombligo", "bajo la cama", "la rama de un árbol", "dentro de un zapato", "dentro de una maleta", "debajo del sofá", "dentro de un armario", "en un bolsillo", "en la bañera llena de espuma", "dentro de un refrigerador", "una montaña rusa", "un castillo encantado", "una casa del árbol", "una tienda de campaña", "un estadio de fútbol", "una pista de patinaje", "un aeropuerto", "un museo de arte", "un acuario", "un parque de diversiones"]

# animal = ["perro", "gato", "caballo", "vaca", "oveja", "cerdo", "gallina", "pato", "conejo", "pez dorado", "león", "tigre", "elefante", "jirafa", "cebra", "gorila", "chimpancé", "hipopótamo", "rinoceronte", "cocodrilo", "delfín", "ballena", "tiburón", "pulpo", "medusa", "caballito de mar", "estrella de mar",
# "morsa", "foca", "pingüino", "ornitorrinco", "perezoso", "armadillo", "narval", "axolotl", "dragón de Komodo", "quokka", "okapi", "australiano casuario", "pangolín", "lémur", "suricato", "mono tití", "canguro", "koala", "gallina de guinea", "mapache", "zarigüeya", "tarsier", "ratón espinoso"]

# food = ["pizza", "hamburguesa", "tacos", "sushi", "pasta", "ensalada", "sándwich", "sopa", "pollo asado", "bistec", "arroz con frijoles", "ceviche", "curry", "paella", "empanadas", "lasagna", "quesadilla", "tamales", "guacamole", "panqueques", "papas fritas", "nachos", "palomitas de maíz", "pretzels", "cacahuates", "chips de tortilla", "galletas", "donas", "churros", "helado", "tacos de langosta", "pizza de sushi", "hamburguesa vegana", "ensalada de quinoa", "sopa de miso", "arroz frito con piña", "pollo teriyaki", "ceviche de mango", "pasta al pesto", "chocolate caliente con chile", "gelatina de pescado", "pizza con helado", "hamburguesa de gominolas", "sándwich de espaguetis", "palomitas con salsa de soya", "sopa de chicle", "tacos de gomitas", "ensalada de caramelos", "pasta con chocolate", "fruta en escabeche"]

# profession = ["doctor", "ingeniero", "abogado", "maestro", "enfermero", "arquitecto", "policía", "bombero", "contable", "dentista", "veterinario", "electricista", "plomero", "carpintero", "piloto", "chef", "diseñador gráfico", "programador", "psicólogo", "científico", "biólogo marino", "astronauta", "fotógrafo", "escritor", "actor", "catador de helados derretidos", "organizador de desfiles de patos", "diseñador de sombreros para mascotas", "experto en selfies", "probador de camas elásticas", "entrenador de caracoles", "crítico de música de ascensor",
#              "especialista en siestas", "inventor de palabras nuevas", "pintor de nubes", "guía turístico de sueños", "coleccionista de rayos de sol", "decorador de iglús", "sommelier de refrescos", "cazador de arcoíris", "mago de burbujas", "compositor de silencios", "consultor de moda para robots", "arquitecto de castillos de arena", "director de orquesta de grillos", "constructor de puentes arcoíris", "editor de historias de fantasmas", "explorador de planetas imaginarios", "fotógrafo de sombras", "cazador de estrellas fugaces"]

# bodypart = ["cabeza", "ojos", "nariz", "boca", "orejas", "cuello", "hombros", "brazos", "manos", "dedos", "pecho", "espalda", "abdomen", "cintura", "caderas", "piernas", "rodillas", "tobillos", "pies", "dedos del pie", "clavícula", "omóplato", "fémur", "tibia", "peroné", "húmero", "radio",
#            "cúbito", "costillas", "mandíbula", "entrecejo", "nudillos", "pantorrilla", "talón de Aquiles", "muñeca", "palma", "planta del pie", "axila", "ombligo", "escalpelo", "corazón", "pulmones", "hígado", "riñones", "estómago", "intestinos", "páncreas", "vesícula biliar", "bazo", "diafragma"]

# color = ["rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosa", "marrón", "negro", "blanco", "gris", "turquesa",
#         "lila", "fucsia", "dorado", "plateado", "vino", "lavanda", "cian", "magenta", "beige", "ocre", "salmón", "coral", "esmeralda"]

# Conjuntos
# name = set(name)
# age = set(age)
# country = set(country)
# place = set(place)
# animal = set(animal)
# food = set(food)
# profession = set(profession)
# bodypart = set(bodypart)
# color = set(color)

# Listas
# name = list(name)
# age = list(age)
# country = list(country)
# place = list(place)
# animal = list(animal)
# food = list(food)
# profession = list(profession)
# bodypart = list(bodypart)
# color = list(color)

# print(f"""
# A sus {age[-1]} años {name[-1]} se fue de viaje a {country[-1]}. Su trabajo de {profession[-1]} le permitió
# visitar este lejano lugar en el que pudo comer {food[-1]}. Lamentablemente terminó visitando
# al doctor ya que su {bodypart[-1]} se hinchó y se puso de color {color[-1]} por estar jugando
# con un/una {animal[-1]} que casualmente encontró en {place[-1]}
#                                                                                [fin..]
# """)


# ===================================================================================================================================================================
# 6. Desglosando el RFC
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente le pedirá al usuario que
# escriba su rfc. El programa deberá crear una tupla con la información desglosada
# del rfc. Al final presentará en pantalla toda la información de la tupla.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("")
# print("="*80)
# print("")
# print(("Bienvenido(A) al \'Analizador de RFC's\'"))
# print("")
# print("="*80)
# print("")
# rfc = input("Por favor Ingresa tu RFC: ")
# print("")
# print("")
# 0123456789012
# DIOOYYMMDD123
# first_lastname = rfc[0:2]
# sec_lastname = rfc[2:3]
# ini_name = rfc[3:4]
# year = rfc[4:6]
# month = rfc[6:8]
# day = rfc[8:10]
# identifier = rfc[10:13]
# print(f"Las primeras dos letras de tu primer apellido son: {first_lastname}")
# print(f"La Inicial de tu segundo apellido es: {sec_lastname}")
# print(f"La inicial de tu primer nombre es: {ini_name}")
# print(f"Tu año de nacimiento es: {year}")
# print(f"Tu mes de nacimiento es: {month}")
# print(f"Tu dia de nacimiento es: {day}")
# print(f"La homoclave de tu RFC es: {identifier}")
# print("")
# print("")
# print("-"*80)


# ===================================================================================================================================================================
# 7. Generador de exámenes/encuestas
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente le pedirá al usuario cuantas
# preguntas quiere para su cuestionario. El programa seleccionará esa cantidad de preguntas de manera
# aleatoria de una lista llena de preguntas (creada por usted). La salida en pantalla será el listado de
# preguntas.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 8. Cifrador chafa chafa
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente le pedirá al usuario el
# mensaje que debe cifrar. El programa invertira el orden de todas las palabras del mensaje y presentará
# el resultado en pantalla
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 9. Cifrador chafa chafa 2
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente le pedirá al usuario el
# mensaje que debe cifrar. El programa invertira el orden de todas las palabras y letras de la palabra del
# mensaje y presentará el resultado en pantalla.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 10. Calculadora de cuenta de restaurante
# El programa pregunte al usuario cuantos comensales y posteriormente pregunte la cantidad de dinero
# que cada comensal debe. Al final pregunta cuanto se quiere dejar de propina. Se debe mostrar en
# pantalla toda la información.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 11. Calculadora
# El programa pregunta dos números y el resultado por renglón son el calculo de sumar, restar, divir,
# multiplicar entre esos dos números.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 12. Calculadora de retiro
# El programa pregunta que edad tienes y a que edad te quieres retirar, al final el programa
# debe presentar: Aún te faltan n años para retirarte. Estamos en 2019 así que te podrás retirar en año
# calculado.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 13. Calculadora de conversión de pesos a dólares, euros, libras y yenes
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 14. Calculadora de conversión de grados farenheit a celcius.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ===================================================================================================================================================================
# 15. Generador de exámenes con opción múltiple
# Tanto el orden de las preguntas como sus respuestas deben ser aleatorias.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
