import struct
# Creamos una cadena binaria
binary_data = struct.pack('3s i f', b'foo', 42, 3.14)
# Escribimos la cadena en un archivo binario
file = open('test.bin', 'wb')
file.write(binary_data)
file.close()
