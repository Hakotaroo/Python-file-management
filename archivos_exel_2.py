# Cargar el archivo existente
wb = openpyxl.load_workbook('estadisticas_jefes.xlsx')
hoja = wb['Estadísticas Jefes']
# Imprimir los datos fila por fila
for fila in hoja.iter_rows(min_row=1, values_only=True):
    print(fila)
