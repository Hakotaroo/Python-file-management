# Crear un archivo binario y escribir datos
with open('test.bin', 'wb') as archivo_bin:
    datos = bytearray([120, 3, 255, 0, 100])  # Datos binarios representando un juego de bytes
    archivo_bin.write(datos)

print("Archivo binario creado con éxito.")
