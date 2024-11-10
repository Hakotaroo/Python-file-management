import csv

# Datos de ejemplo sobre jefes de juegos tipo Souls
jefes = [
    ['Nombre', 'Vida', 'Localización'],
    ['Gwyn, Lord of Cinder', 6000, 'Kiln of the First Flame'],
    ['Artorias, the Abysswalker', 5200, 'Oolacile'],
    ['Siegmeyer of Catarina', 4000, 'Ash Lake']
]

# Escribir datos en un archivo CSV
with open('jefes_souls.csv', 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    for jefe in jefes:
        escritor.writerow(jefe)

print("Archivo CSV creado y escrito con éxito.")
