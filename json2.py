# Leer datos desde el archivo JSON
with open('jefes_souls.json', 'r') as archivo_json:
    datos_cargados = json.load(archivo_json)

# Imprimir detalles de los jefes
for jefe in datos_cargados['jefes']:
    print(f"Jefe: {jefe['nombre']}, Vida: {jefe['vida']}, Localización: {jefe['localizacion']}")
