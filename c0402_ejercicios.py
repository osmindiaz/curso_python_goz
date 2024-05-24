# 1. Escribe un programa que le pida su nombre al usuario y como salida le diga cuantos caracteres tiene su nombre.
# -------------------------------------------------------------------------------------------------------------------------
# name = input("Ingresa tu nombre: ")
# print("Hola "+name+", tu nombre tiene "+str(len(name))+" caracteres!")

# 2. Escribe un programa que le pida primero su nombre al usuario, posteriormente su apellido, crea una variable de nombre
# completo concatenando el nombre y el apellido y muestra en pantalla
# -------------------------------------------------------------------------------------------------------------------------
# name = input("Ingresa tu nombre: ")
# lastname = input("Ingresa tu apedillo XD: ")
# print("Mi estimado o estimada, pero jamas estimade, tu nombre completo es: "+name+" "+lastname)

# 3. Escribe un programa que le pida primero el nombre de su deporte favorito, posteriormente se le pide al usuario su edad.
# Muestra en pantalla el nombre del deporte el número de veces igual a la edad del usuario.
# -------------------------------------------------------------------------------------------------------------------------
# hobbie = input("Oye tu, sí, tu, cual es tu deporte favorito?: ")
# age = input("Ahora dime tu edad: ")
# print("Checate esto: "+f"\n{hobbie} "*int(age))

# 4. Escribe un programa que al proporcionarle la siguiente clave HomeroSimpson1970SpringfieldUSA nos guarde el nombre, apellido, año, estado y país en variables independientes y
# porteriormente muestra en pantalla un mensaje de bienvenida utilizando las variables.
# -------------------------------------------------------------------------------------------------------------------------
# print(len(password))
# 0123456789012345678901234567890
# HomeroSimpson1970SpringfieldUSA
# password = input("Ingresa la Clave: ")
# name = password[0:5]
# lastname = password[6: 13]
# year = password[13:17]
# city = password[17:28]
# country = password[28:]
# print(f"Name: {name}")
# print(f"Lastname: {lastname}")
# print(f"Year: {year}")
# print(f"City: {city}")
# print(f"Country: {country}")

# 5. Escribe un programa que te permita ingresar dos numeros enteros y como salida de el resultado de la suma.
# -------------------------------------------------------------------------------------------------------------------------
# a = int(input("Ingresa un numero: "))
# b = int(input("Ingresa otro numero: "))
# sum = a+b
# print("La suma es: " + str(sum))

# 6. Escribe un programa que te permita ingresar dos numeros enteros y como salida de el resultado de concatenar los dos números.
# -------------------------------------------------------------------------------------------------------------------------
# x = int(input("Ingresa el numero x: "))
# y = int(input("Ingresa el numero y: "))
# concat = (str(x)+str(y))
# print(concat)

# 7. Escribe un programa que te permita ingresar una cadena de texto y el resultado sea esa misma cadena pero en orden totalmente invertido.
# -------------------------------------------------------------------------------------------------------------------------
# reverse = (str(input("Ingresa una palabra o frase matona: ")))
# print(reverse[::-1])

# 8. Escribe un programa que te permita ingresar una cadena de texto, porteriormente el programa solicita una cadena a reemplazar,
# y luego solicita el valor por el cual se reemplazara, como resultado el programa presenta la cadena original pero con el reemplazo indicado.
# -------------------------------------------------------------------------------------------------------------------------
# phrase = str(input("Ingresa una frase: "))
# incorrect = str(input("Existe un error, ingresa la parte a corregir: "))
# correction = str(input("Ingresa la correccion: "))
# corrected = phrase.replace(incorrect, correction)
# print(f"Esta fue tu frase inicial: {phrase}")
# print(f"Esta es la frase corregida: {corrected}")

# 9. Escribe un programa que te permita ingresar una cadena de texto y la salida sea la misma cadena pero con todas las letras en mayúsculas.
# -------------------------------------------------------------------------------------------------------------------------
# phrase = str(input("Escribe una frase: "))
# print(str.upper(phrase))

# 10. Escribe un programa que te permita ingresar una cadena de texto y el programa indique si la cadena tiene esta formada por caracteres numéricos.
# -------------------------------------------------------------------------------------------------------------------------
# text = input("Ingresa algo aqui: ")
# print(type(text))
# print("Is the input a Integer?: ", (isinstance(text, int)))

# 11. Escribe un program que te permita ingresar una cadena de texto y el programa indique si la cadena esta formada solamente por letras en mayúsculas.
# -------------------------------------------------------------------------------------------------------------------------
# text = input("Ingresa algo aqui: ")
# print("Is the text UPPER?: ", (text.isupper()))

# 12. Escribe un programa que te haga preguntas para ordenar una pizza y al final se muestre el resumen del pedido.
# -------------------------------------------------------------------------------------------------------------------------
# print("")
# print("Bienvenidos a la pizzeria \"EL PIZZERO COQUETO\"  por favor completa el siguiente formulario:")
# print("")
# name = input("Ingresa tu nombre: ")
# gender = input("Ingresa tu Genero: \"Masculino\", \"Femenino\": ")
# if gender == "Femenino":
#    bf = input("Tienes novio? \"Si\" , \"No\": ")
#    if bf == "Si":
#        danger = input("Y esta muy grande? \"Si\" , \"No\": ")
# qty = input("Cuantas pizzas quieres?: ")
# size = input("Ingresa el tamaño de tu pizza: ")
# type = input("ingresa el tipo de pizza que quieres: ")
# print("")
# print("Gracias por la informacion, este es el resumen de tu pedido;")
# print("")
# print(f"Pedido para: {name}")
# print("-"*20)
# print(f"Te enviaremos {qty} pizza(s) {size} (s) de {type}")
# print("-"*20)
# if gender == "Femenino" and bf == "No":
#    print("Que te parece si invito a ver una pelicula mientras comemos la pizza")
# elif gender == "Femenino" and bf == "Si" and danger == "No":
#    print(f"Oh, tienes novio, igual te invito a salir")
# elif gender == "Femenino" and bf == "Si" and danger == "Si":
#    print("Te invito a salir, tu novio podra estar grandote pero yo soy muy valiente")

# 13. Escribe un programa que te permita ingresar el nombre de una película y como salida muestre el último caracter de la cadena.
# -------------------------------------------------------------------------------------------------------------------------
# movie_title = input("Ingresa el nombre de una pelicula: ")
# print(movie_title[-1])

# 14. Generador de cuentos - El programa al iniciar debe presentar un mensaje de saludo, posteriormente comenzará a preguntarle al usuario
# lo siguiente: el nombre del usuario, edad, lugar, animal, país, comida, color, profesión, parte del cuerpo.
# La salida del programa debe ser un cuento con la siguiente estructura:
# A sus edad años nombre se fue de viaje a país. Su trabajo de profesión le permitió
# visitar este lejano lugar en el que pudo comer comida. Lamentablemente terminó visitando
# al doctor ya que su parte del cuerpo se hinchó y se puso de color color por estar jugando
# con un/una animal que casualmente encontró en un lugar
# -------------------------------------------------------------------------------------------------------------------------
# name = input("Ingresa un nombre: ")
# age = input("Ingresa una edad: ")
# country = input("ingresa un pais: ")
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
# """)


# 15. Mensajes secretos - El programa al iniciar debe presentar un saludo y posteriormente solicitar el ingreso de un mensaje.
# La salida del programa debera mostrar la cadena pero haciendo las siguientes sustituciones:
# a = 4, e = 3, i = 1, o = 0
# -------------------------------------------------------------------------------------------------------------------------
# print("")
# print("Bienvenido agente 00-chapucero, estamos listos para recibir su mensaje...")
# print("")
# message = input("Mensaje a codificar: ")
# message = message.replace("a", "4").replace("A", "4")
# message = message.replace("e", "3").replace("E", "3")
# message = message.replace("i", "1").replace("I", "1")
# message = message.replace("o", "0").replace("O", "0")
# print("")
# print(f"Este es su mensaje cifrado: {message}")
# print("")
