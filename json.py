import json

# Datos de ejemplo de un juego tipo Souls con detalles de jefes
datos_juego = {
    'juego': 'Dark Souls III',
    'jefes': [
        {'nombre': 'Abyss Watchers', 'vida': 4500, 'localizacion': 'Farron Keep'},
        {'nombre': 'Yhorm the Giant', 'vida': 10000, 'localizacion': 'Profaned Capital'},
        {'nombre': 'Nameless King', 'vida': 7500, 'localizacion': 'Archdragon Peak'}
    ]
}

# Escribir datos en un archivo JSON
with open('jefes_souls.json', 'w') as archivo_json:
    json.dump(datos_juego, archivo_json, indent=4)

print("Archivo JSON creado y escrito con éxito.")
