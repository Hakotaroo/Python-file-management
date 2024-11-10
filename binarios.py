import struct
# Leemos el contenido del archivo binario	
file = open('test.bin', 'rb')
binary_data = file.read()
file.close()
# Desempaquetamos la cadena binaria
unpacked_data = struct.unpack('3s i f', binary_data)
print(unpacked_data)
