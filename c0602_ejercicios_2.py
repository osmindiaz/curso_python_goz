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
# from decimal import *
# print("")
# print("="*80)
# print("")
# print(("Bienvenido(A) al \'cuenta cuentos 3000 PRO ULTRA\', por favor ingresa los siguientes datos").upper())
# print("")
# print("="*80)
# print("")

# -------------------------------Listas
# name = ["Alejandro", "Beatriz", "Carlos", "Dolores", "Elena", "Francisco", "Gabriela", "Hernán", "Isabel", "Javier", "Karla", "Luis", "María",
#        "Natalia", "Óscar", "Patricia", "Quintín", "Raquel", "Santiago", "Teresa", "Ulises", "Valeria", "Wilfredo", "Ximena", "Yolanda", "Zacarías"]

# age = [61, 64, 38, 17, 73, 59, 27, 37, 47, 16, 56, 41, 26, 60, 48, 53, 32, 18, 52, 57, 50, 36, 62, 55, 42, 21, 25, 67, 58, 44,
#       39, 29, 46, 54, 33, 71, 28, 65, 66, 49, 23, 24, 31, 72, 43, 69, 20, 68, 74, 30, 45, 63, 34, 75, 51, 40, 22, 35, 15, 70, 19]

# country = ["Argentina", "Brasil", "Chile", "Colombia", "México", "Perú", "Venezuela", "Uruguay", "Paraguay", "Bolivia", "Ecuador", "Guatemala", "Honduras", "El Salvador", "Nicaragua", "Costa Rica", "Panamá", "Cuba", "República Dominicana", "Puerto Rico", "España", "Portugal", "Francia", "Italia", "Alemania",
#           "Reino Unido", "Países Bajos", "Bélgica", "Suiza", "Austria", "Suecia", "Noruega", "Dinamarca", "Finlandia", "Islandia", "Rusia", "China", "Japón", "Corea del Sur", "India", "Australia", "Nueva Zelanda", "Sudáfrica", "Egipto", "Marruecos", "Nigeria", "Kenya", "Turquía", "Israel", "Arabia Saudita"]

# place = ["cocina", "recámara", "baño", "sala", "comedor", "sótano", "ático", "garaje", "pasillo", "jardín trasero", "parque", "biblioteca", "restaurante", "cine", "escuela", "supermercado", "hospital", "estación de policía", "bomberos", "gimnasio", "el espacio", "Marte", "la cima de un volcán", "el fondo del océano", "un desierto", "el Triángulo de las Bermudas", "una isla desierta", "la Luna", "el Polo Norte", "el Amazonas",
#         "dentro del ombligo", "bajo la cama", "la rama de un árbol", "dentro de un zapato", "dentro de una maleta", "debajo del sofá", "dentro de un armario", "en un bolsillo", "en la bañera llena de espuma", "dentro de un refrigerador", "una montaña rusa", "un castillo encantado", "una casa del árbol", "una tienda de campaña", "un estadio de fútbol", "una pista de patinaje", "un aeropuerto", "un museo de arte", "un acuario", "un parque de diversiones"]

# animal = ["perro", "gato", "caballo", "vaca", "oveja", "cerdo", "gallina", "pato", "conejo", "pez dorado", "león", "tigre", "elefante", "jirafa", "cebra", "gorila", "chimpancé", "hipopótamo", "rinoceronte", "cocodrilo", "delfín", "ballena", "tiburón", "pulpo", "medusa", "caballito de mar", "estrella de mar",
#          "morsa", "foca", "pingüino", "ornitorrinco", "perezoso", "armadillo", "narval", "axolotl", "dragón de Komodo", "quokka", "okapi", "australiano casuario", "pangolín", "lémur", "suricato", "mono tití", "canguro", "koala", "gallina de guinea", "mapache", "zarigüeya", "tarsier", "ratón espinoso"]

# food = ["pizza", "hamburguesa", "tacos", "sushi", "pasta", "ensalada", "sándwich", "sopa", "pollo asado", "bistec", "arroz con frijoles", "ceviche", "curry", "paella", "empanadas", "lasagna", "quesadilla", "tamales", "guacamole", "panqueques", "papas fritas", "nachos", "palomitas de maíz", "pretzels", "cacahuates", "chips de tortilla", "galletas", "donas", "churros", "helado", "tacos de langosta", "pizza de sushi",
#        "hamburguesa vegana", "ensalada de quinoa", "sopa de miso", "arroz frito con piña", "pollo teriyaki", "ceviche de mango", "pasta al pesto", "chocolate caliente con chile", "gelatina de pescado", "pizza con helado", "hamburguesa de gominolas", "sándwich de espaguetis", "palomitas con salsa de soya", "sopa de chicle", "tacos de gomitas", "ensalada de caramelos", "pasta con chocolate", "fruta en escabeche"]

# profession = ["doctor", "ingeniero", "abogado", "maestro", "enfermero", "arquitecto", "policía", "bombero", "contable", "dentista", "veterinario", "electricista", "plomero", "carpintero", "piloto", "chef", "diseñador gráfico", "programador", "psicólogo", "científico", "biólogo marino", "astronauta", "fotógrafo", "escritor", "actor", "catador de helados derretidos", "organizador de desfiles de patos", "diseñador de sombreros para mascotas", "experto en selfies", "probador de camas elásticas", "entrenador de caracoles", "crítico de música de ascensor",
#              "especialista en siestas", "inventor de palabras nuevas", "pintor de nubes", "guía turístico de sueños", "coleccionista de rayos de sol", "decorador de iglús", "sommelier de refrescos", "cazador de arcoíris", "mago de burbujas", "compositor de silencios", "consultor de moda para robots", "arquitecto de castillos de arena", "director de orquesta de grillos", "constructor de puentes arcoíris", "editor de historias de fantasmas", "explorador de planetas imaginarios", "fotógrafo de sombras", "cazador de estrellas fugaces"]

# bodypart = ["cabeza", "ojos", "nariz", "boca", "orejas", "cuello", "hombros", "brazos", "manos", "dedos", "pecho", "espalda", "abdomen", "cintura", "caderas", "piernas", "rodillas", "tobillos", "pies", "dedos del pie", "clavícula", "omóplato", "fémur", "tibia", "peroné", "húmero", "radio",
#            "cúbito", "costillas", "mandíbula", "entrecejo", "nudillos", "pantorrilla", "talón de Aquiles", "muñeca", "palma", "planta del pie", "axila", "ombligo", "escalpelo", "corazón", "pulmones", "hígado", "riñones", "estómago", "intestinos", "páncreas", "vesícula biliar", "bazo", "diafragma"]

# color = ["rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosa", "marrón", "negro", "blanco", "gris", "turquesa",
#         "lila", "fucsia", "dorado", "plateado", "vino", "lavanda", "cian", "magenta", "beige", "ocre", "salmón", "coral", "esmeralda"]

# -------------------------------Conjuntos
# name = set(name)
# age = set(age)
# country = set(country)
# place = set(place)
# animal = set(animal)
# food = set(food)
# profession = set(profession)
# bodypart = set(bodypart)
# color = set(color)

# -------------------------------Listas
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
#                                                                               [fin..]
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
# print("")
# print("="*80)
# print("")
# print("Bienvenido(A) al la encuesta de satisfaccion al cliente de \'Pizza Python\'")
# print("")
# print("="*80)
# print("")
# qty = int(input("Cuantas preguntas podras contestar, Max 28: "))

# questions = [
#    '¿Con qué frecuencia ordenas pizzas de nuestra compañía?',
#    '¿Cómo evaluas la facilidad de uso de nuestro sitio web o aplicación móvil para realizar pedidos?',
#    '¿Cuánto tiempo suele tardar en llegar tu pedido?',
#    '¿Estás satisfecho con el tiempo de entrega de tu pedido?',
#    '¿La pizza llegó caliente y en buenas condiciones?',
#    '¿Cómo calificas la calidad de nuestras pizzas?',
#    '¿Qué tan variado te parece nuestro menú?',
#    '¿Encuentras satisfactorias nuestras opciones de personalización de pizzas?',
#    '¿Cómo calificas la relación calidad-precio de nuestras pizzas?',
#    '¿Cómo evalúas la atención al cliente proporcionada por nuestro personal?',
#    '¿Has tenido algún problema con tu pedido en los últimos seis meses?',
#    '¿Qué tan satisfecho estás con las promociones y ofertas que ofrecemos?',
#    '¿Qué tan fácil es para ti encontrar información sobre nuestras promociones y ofertas?',
#    '¿Qué tan probable es que recomiendes nuestras pizzas a amigos o familiares?',
#    '¿Cómo calificarías la limpieza y presentación de nuestras tiendas?',
#    '¿Qué tan satisfecho estás con la variedad de opciones de bebidas disponibles?',
#    '¿Qué tan satisfecho estás con la variedad de opciones de postres disponibles?',
#    '¿Qué tan satisfecho estás con la opción de seguimiento de pedidos en tiempo real?',
#    '¿Qué tan satisfecho estás con el empaque de nuestras pizzas?',
#    '¿Qué tan satisfecho estás con la opción de pago en línea?',
#    '¿Qué tan fácil es para ti encontrar información sobre nuestros ingredientes y alérgenos?',
#    '¿Cómo calificas la amabilidad y cortesía de nuestros repartidores?',
#    '¿Qué tan satisfecho estás con la opción de pedidos anticipados?',
#    '¿Has tenido alguna vez una experiencia negativa con nuestro servicio de entrega?',
#    '¿Qué tan satisfecho estás con la calidad y frescura de nuestros ingredientes?',
#    '¿Qué tan satisfecho estás con el tamaño de las porciones de nuestras pizzas?',
#    '¿Qué tan satisfecho estás con la opción de recogida en tienda?',
#    '¿Tienes algún comentario o sugerencia adicional para mejorar nuestro servicio?'
# ]
# questions = set(questions)
# questions = list(questions)


# ===================================================================================================================================================================
# 8. Cifrador chafa chafa
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente le pedirá al usuario el
# mensaje que debe cifrar. El programa invertira el orden de todas las palabras del mensaje y presentará
# el resultado en pantalla
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("")
# print("="*80)
# print("")
# print('Este programa te ayudara de la manera mas chafa a \"Cifrar\" un mensaje v1')
# print("")
# print("="*80)
# print("")
# message = input('Ingresa el mensaje que quieres \"Cifrar\": ')


# ===================================================================================================================================================================
# 9. Cifrador chafa chafa 2
# El programa al iniciar debe presentar un mensaje de saludo, posteriormente le pedirá al usuario el
# mensaje que debe cifrar. El programa invertira el orden de todas las palabras y letras de la palabra del
# mensaje y presentará el resultado en pantalla.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("")
# print("="*80)
# print("")
# print('Este programa te ayudara de la manera mas chafa a \"Cifrar\" un mensaje v2')
# print("")
# print("="*80)
# print("")
# message = input('Ingresa el mensaje que quieres \"Cifrar\": ')
# print("")
# print(f'Este es tu mensaje \"Cifrado\": {message[::-1]}')
# print("")
# print("-"*80)
# print("")


# ===================================================================================================================================================================
# 10. Calculadora de cuenta de restaurante
# El programa pregunte al usuario cuantos comensales y posteriormente pregunte la cantidad de dinero
# que cada comensal debe. Al final pregunta cuanto se quiere dejar de propina. Se debe mostrar en
# pantalla toda la información.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from decimal import *

# print("")
# print("="*80)
# print("")
# print('Calculadora \"No se hagan patos\" - para la cuenta')
# print("")
# print("="*80)
# print("")
# guests = int(input("Ingresa la cantidad de comensales: "))
# check = Decimal(input("Ingresa la cantidad de la cuenta: "))
# tip08 = Decimal(check)*Decimal(.08)
# tip10 = Decimal(check)*Decimal(.10)
# tip15 = Decimal(check)*Decimal(.15)
# tip20 = Decimal(check)*Decimal(.20)
# print("")
# print("La propina sugerida es de: ")
# print(f"Los atendieron terriblemente y los insultaron y hasta sospenchan que les escupieron en el plato :( \t-\t 0%\t-\t$0.00")
# print(
#    f"Los trataron regular, no asi que digas, ah que bruto como nos les importamos a estos cuates        \t-\t 8%\t-\t${tip08:,.2f}")
# print(
#    f"El servicio estuvo bien, trajeron la comida a tiempo, se porto amable el mesero o mesera           \t-\t10%\t-\t${tip10:,.2f}")
# print(
#    f"El servicio estuvo super, todo estaba muy rico y muy rapido, muy buen servicio la verdad           \t-\t15%\t-\t${tip15:,.2f}")
# print(
#    f"Nos trataron como reyes, la comida deliciosa, el lugar impecable y aparte la mesera guapisima      \t-\t20%\t-\t${tip20:,.2f}")
# print("")
# tip = Decimal(input("Cuanto van a dejar de propina?: "))
# total = (Decimal(check)+Decimal(tip))
# split = (Decimal(total)/Decimal(guests))
# print("")
# print("-"*80)
# print("")
# print(f"El total para su consumo de: ${
#      check:,.2f} + ${tip:,.2f} es de: ${total:,.2f}")
# print("")
# print(f"Dividido entre {guests} comensales, les toca de ${
#      split:,.2f} por persona.")
# print("")


# ===================================================================================================================================================================
# 11. Calculadora
# El programa pregunta dos números y el resultado por renglón son el calculo de sumar, restar, divir,
# multiplicar entre esos dos números.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from decimal import *
# print("")
# print("="*80)
# print("")
# print('Calculadora Simple')
# print("")
# print("="*80)
# print("")
# number01 = Decimal(input("Ingresa un Numero: "))
# number02 = Decimal(input("Ingresa Otro Numero: "))
# print("")
# print(f"Suma\t\t-\t{number01} + {number02} = {number01+number02:,.2f}")
# print(f"Resta\t\t-\t{number01} - {number02} = {number01-number02:,.2f}")
# print(f"Multiplicacion\t-\t{number01} x {number02} = {number01*number02:,.2f}")
# print(f"Division\t-\t{number01} / {number02} = {number01/number02:,.2f}")
# print("")
# print("-"*80)


# ===================================================================================================================================================================
# 12. Calculadora de retiro
# El programa pregunta que edad tienes y a que edad te quieres retirar, al final el programa
# debe presentar: Aún te faltan n años para retirarte. Estamos en 2024 así que te podrás retirar en año
# calculado.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from datetime import datetime
# print("")
# print("="*80)
# print("")
# print('Calculadora para el Retiro')
# print("")
# print("="*80)
# print("")
# now = datetime.now()
# now = now.year
# age = int(input("Ingresa tu edad: "))
# retirement = int(input("A que edad piensas retirarte?: "))
# print("")
# print("-"*80)
# print("")
# timeleft = retirement-age
# print(f"Te faltan {timeleft} años para retirarte")
# print(f"Tu año de retiro será: {now+timeleft}")
# print("")
# print("-"*80)
# print("")


# ===================================================================================================================================================================
# 13. Calculadora de conversión de pesos a dólares, euros, libras y yenes
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from decimal import *
# print("")
# print("="*80)
# print("")
# print('CONVERTIDOR DE DIVISAS')
# print("")
# print("="*80)
# mxn_rate = 1
# usd_rate = 16.97
# eur_rate = 18.40
# gbp_rate = 21.61
# jpy_rate = 0.11
# -----------------------------------------------------------------------------------------------------------------------Data Input----
# print("CODIGOS DE MONEDA \n\t - Para pesos: MXN\n\t - Para Dolares: USD\n\t - Para Euros: EUR\n\t - Para Libras: GBP\n\t - Para Yenes: JPY\n")
# ammount2convert = Decimal(input("\t\t\tIngresa el monto a convertir: "))
# from_currency = input("\t\t\tSelecciona el codigo de moneda inicial: ")
# from_currency = from_currency.upper()
# to_currency = input("\t\t\tIngresa el codigo de moneda objetivo: ")
# to_currency = to_currency.upper()
# divider = ("-"*80)
# --------------------------------------------------------------------------------------------------------------------Convert From MXN----
# if from_currency == "MXN":
#    if to_currency == "MXN":
#        converted = Decimal(ammount2convert)/Decimal(mxn_rate)
#        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#              converted:,.4f} {to_currency}\n\n{divider}")
#    else:
#        if to_currency == "USD":
#            converted = Decimal(ammount2convert)/Decimal(usd_rate)
#            print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                converted:,.4f} {to_currency}\n\n{divider}")
#        else:
#            if to_currency == "EUR":
#                converted = Decimal(ammount2convert)/Decimal(eur_rate)
#                print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                    converted:,.4f} {to_currency}\n\n{divider}")
#            else:
# if to_currency == "GBP":
#                    converted = Decimal(ammount2convert)/Decimal(gbp_rate)
#                    print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                        converted:,.4f} {to_currency}\n\n{divider}")
#                else:
#                    if to_currency == "JPY":
#                        converted = Decimal(ammount2convert)/Decimal(jpy_rate)
#                        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                            converted:,.4f} {to_currency}\n\n{divider}")
#                    else:
#                        print(
#                            f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{to_currency}\' que ingresaste no es soportado\n")
# else:
#    if from_currency == "USD":
#        if to_currency == "MXN":
#            converted = Decimal(ammount2convert)*Decimal(usd_rate)
#            print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                  converted:,.4f} {to_currency}\n\n{divider}")
#        else:
#            if to_currency == "USD":
#                converted = ammount2convert
#                print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                    converted:,.4f} {to_currency}\n\n{divider}")
#            else:
#                if to_currency == "EUR":
#                    convert_to_mxn = Decimal(ammount2convert)*Decimal(usd_rate)
#                    converted = Decimal(convert_to_mxn)/Decimal(eur_rate)
#                    print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                        converted:,.4f} {to_currency}\n\n{divider}")
#                else:
#                    if to_currency == "GBP":
#                        convert_to_mxn = Decimal(
#                            ammount2convert)*Decimal(usd_rate)
#                        converted = Decimal(convert_to_mxn)/Decimal(gbp_rate)
#                        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                            converted:,.4f} {to_currency}\n\n{divider}")
#                    else:
#                        if to_currency == "JPY":
#                            convert_to_mxn = Decimal(
#                                ammount2convert)*Decimal(usd_rate)
#                            converted = Decimal(
#                                convert_to_mxn)/Decimal(jpy_rate)
#                            print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                  converted:,.4f} {to_currency}\n\n{divider}")
#                        else:
#                            print(
#                                f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{to_currency}\' que ingresaste no es soportado\n")
#    else:
#        if from_currency == "EUR":
#            if to_currency == "MXN":
#                converted = Decimal(ammount2convert)*Decimal(eur_rate)
#                print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                      converted:,.4f} {to_currency}\n\n{divider}")
#            else:
#                if to_currency == "USD":
#                    convert_to_mxn = Decimal(ammount2convert)*Decimal(eur_rate)
#                    converted = Decimal(convert_to_mxn)/Decimal(usd_rate)
#                    print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                        converted:,.4f} {to_currency}\n\n{divider}")
#                else:
#                    if to_currency == "EUR":
#                        convert_to_mxn = Decimal(
#                            ammount2convert)*Decimal(eur_rate)
#                        converted = Decimal(convert_to_mxn)/Decimal(eur_rate)
#                        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                            converted:,.4f} {to_currency}\n\n{divider}")
#                    else:
#                        if to_currency == "GBP":
#                            convert_to_mxn = Decimal(
#                                ammount2convert)*Decimal(eur_rate)
#                            converted = Decimal(
#                                convert_to_mxn)/Decimal(gbp_rate)
#                            print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                converted:,.4f} {to_currency}\n\n{divider}")
#                        else:
#                            if to_currency == "JPY":
#                                convert_to_mxn = Decimal(
#                                    ammount2convert)*Decimal(eur_rate)
#                                converted = Decimal(
#                                    convert_to_mxn)/Decimal(jpy_rate)
#                                print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                    converted:,.4f} {to_currency}\n\n{divider}")
#                            else:
#                                print(
#                                    f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{to_currency}\' que ingresaste no es soportado\n")
#        else:
#            # -------------------------------------------------------------------------------------------------------------------------------------------
#            if from_currency == "GBP":
#                if to_currency == "MXN":
#                    converted = Decimal(ammount2convert)*Decimal(gbp_rate)
#                    print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                        converted:,.4f} {to_currency}\n\n{divider}")
#                else:
#                    if to_currency == "USD":
#                        convert_to_mxn = Decimal(
#                            ammount2convert)*Decimal(gbp_rate)
#                        converted = Decimal(
#                            convert_to_mxn)/Decimal(usd_rate)
#                        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                            converted:,.4f} {to_currency}\n\n{divider}")
#                    else:
#                        if to_currency == "EUR":
#                            convert_to_mxn = Decimal(
#                                ammount2convert)*Decimal(gbp_rate)
#                            converted = Decimal(
#                                convert_to_mxn)/Decimal(eur_rate)
#                            print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                converted:,.4f} {to_currency}\n\n{divider}")
#                        else:
#                            if to_currency == "GBP":
#                                convert_to_mxn = Decimal(
#                                    ammount2convert)*Decimal(gbp_rate)
#                                converted = Decimal(
#                                    convert_to_mxn)/Decimal(gbp_rate)
#                                print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                    converted:,.4f} {to_currency}\n\n{divider}")
#                            else:
#                                if to_currency == "JPY":
#                                    convert_to_mxn = Decimal(
#                                        ammount2convert)*Decimal(gbp_rate)
#                                    converted = Decimal(
#                                        convert_to_mxn)/Decimal(jpy_rate)
#                                   print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                       converted:,.4f} {to_currency}\n\n{divider}")
#                                else:
#                                    print(
#                                        f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{to_currency}\' que ingresaste no es soportado\n")
#            else:
#                # -------------------------------------------------------------------------------------------------------------------------------------------
#                if from_currency == "JPY":
#                    if to_currency == "MXN":
#                        converted = Decimal(ammount2convert)*Decimal(jpy_rate)
#                        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                            converted:,.4f} {to_currency}\n\n{divider}")
#                    else:
#                        if to_currency == "USD":
#                            convert_to_mxn = Decimal(
#                                ammount2convert)*Decimal(jpy_rate)
#                            converted = Decimal(
#                                convert_to_mxn)/Decimal(usd_rate)
#                            print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                converted:,.4f} {to_currency}\n\n{divider}")
#                        else:
#                            if to_currency == "EUR":
#                                convert_to_mxn = Decimal(
#                                    ammount2convert)*Decimal(jpy_rate)
#                                converted = Decimal(
#                                    convert_to_mxn)/Decimal(eur_rate)
# print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                    converted:,.4f} {to_currency}\n\n{divider}")
#                            else:
#                                if to_currency == "GBP":
#                                    convert_to_mxn = Decimal(
#                                        ammount2convert)*Decimal(jpy_rate)
#                                    converted = Decimal(
#                                        convert_to_mxn)/Decimal(gbp_rate)
#                                    print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                        converted:,.4f} {to_currency}\n\n{divider}")
#                                else:
#                                    if to_currency == "JPY":
#                                        convert_to_mxn = Decimal(
#                                            ammount2convert)*Decimal(jpy_rate)
#                                        converted = Decimal(
#                                            convert_to_mxn)/Decimal(jpy_rate)
#                                        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
#                                            converted:,.4f} {to_currency}\n\n{divider}")
#                                    else:
#                                        print(
#                                            f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{to_currency}\' que ingresaste no es soportado\n")


# ===================================================================================================================================================================
# 14. Calculadora de conversión de grados farenheit a celcius.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from decimal import *
# print("")
# print("="*80)
# print("")
# print('Calculadora de conversion de temperaturas')
# print("")
# print("="*80)
# degrees = Decimal(input("Por favor ingresa la temperatura: "))
# from_unit = input("\t\tIngresa la unidad de Origen (\'F\' o \'C\'): ")
# to_unit = input("\t\tIngresa la unidad de Destino (\'F\' o \'C\'): ")
# from_unit = from_unit.lower()
# to_unit = to_unit.lower()

# if from_unit == "f":
#    if to_unit == "c":
#        result = (Decimal(degrees)-Decimal(32))*Decimal(.5556)
#        print(f"\n\t\t{degrees}°{from_unit} = {result:,.2f}°{to_unit}\n")
#    else:
#        if to_unit == 'f':
#            result = degrees
#            print(f"\n\t\t{degrees}°{from_unit} = {result:,.2f}°{to_unit}\n")
#        else:
#            print(f"\n\t\tla unidad destino: \'{to_unit}\' no existe \n")
# elif from_unit == "c":
#    if to_unit == "f":
#        result = (Decimal(degrees)*Decimal(1.8))+Decimal(32)
#        print(f"\n\t\t{degrees}°{from_unit} = {result:,.2f}°{to_unit}\n")
#    else:
#        if to_unit == 'c':
#            result = degrees
#            print(f"\n\t\t{degrees}°{from_unit} = {result:,.2f}°{to_unit}\n")
#        else:
#            print(f"\n\t\tla unidad destino: \'{to_unit}\' no existe \n")
# else:
#    print(f"\n\t\tla unidad origen: \'{from_unit}\' no existe \n")

# ===================================================================================================================================================================
# 15. Generador de exámenes con opción múltiple
# Tanto el orden de las preguntas como sus respuestas deben ser aleatorias.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("="*150)
# print('\nBienvenidos al examen mas facil del mundo\n')
# print("="*150)
# questions = [
#    '¿Qué tipo de animal es Marty?',
#    '¿Dónde vivían los animales antes de llegar a Madagascar?',
#    '¿Cómo se llama la jirafa en "Madagascar"?',
#    '¿Qué animal es Gloria?',
#    '¿Quién es el líder de los pingüinos?',
#    '¿Cuál es el nombre del rey lémur en Madagascar?',
#    '¿Qué canción popular canta el rey lémur y los demás animales?',
#    '¿Qué animal es Alex?',
#    '¿Qué tipo de problemas de salud tiene Melman?',
#    '¿Quién es el mejor amigo de Marty?',
#    '¿Por qué los animales terminan en Madagascar?'
# ]
# answers = [
#    'Alex',
#    'Cebra',
# 'En un zoológico en Nueva York',
#    'Melman',
#    'Hipopótamo',
#    'Skipper',
#    'King Julian',
#    'I Like to Move It',
#    'León',
#    'Hipocondría',
#    'Porque su barco se hunde']

# questions = set(questions)
# answers = set(answers)
# questions = list(questions)
# answers = list(answers)


# print("{:<75} {:<75}".format("Questions", "Answers"))
# print("-" * 150)
# for question, answer in zip(questions, answers):
#    print("{:<75} {:<75}".format(question, answer))
