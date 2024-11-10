# Leer el archivo binario
with open('test.bin', 'rb') as archivo_bin:
    contenido = archivo_bin.read()
    print("Contenido del archivo binario:", list(contenido))
