import requests

url = 'https://gccdtapp03.epicorsaas.com/SaaS1037/api/v1/BaqSvc/'
username = input("Ingresa tu usuario: ")
password = input("Ingresa tu password: ")
login_notes = input("Notas de autenticacion: ")


def login_and_check(username, password):
    try:
        response = requests.get(url, auth=(username, password))

        # Prepara el contenido del txt con las respuestas
        content = ("-" * 80 + "\n" + f"{login_notes}\n" +
                   "-" * 80 + "\n" +
                   "Codigo del estado de la respuesta:\n" +
                   f"{response.status_code}\n\n" +
                   "-" * 80 + "\n\n" +
                   "Contenido de la respuesta:\n" +
                   response.text + "\n" +
                   "-" * 80 + "\n\n"
                   )

        # Escribir el txt
        with open("response.txt", "w") as file:
            file.write(content)

        print("El contenido de la respuesta se ha escrito en response.txt")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


login_and_check(username, password)
