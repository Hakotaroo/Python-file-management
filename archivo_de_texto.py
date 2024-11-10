with open('archivo.txt', 'w') as file:
    file.write("Hola, este es un archivo de texto.\n")

with open('archivo.txt', 'r') as file:
    contenido = file.read()
    print(contenido)
