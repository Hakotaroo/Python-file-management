import openpyxl
# Crear un libro de trabajo y una hoja
wb = openpyxl.Workbook()
hoja = wb.active
hoja.title = 'Estadísticas Jefes'
# Añadir encabezados y datos
hoja.append(['Jefe', 'Vida', 'Localización'])
hoja.append(['Gwyn', 6000, 'Kiln of the First Flame'])
hoja.append(['Ornstein y Smough', 8500, 'Anor Londo'])
# Guardar el archivo
wb.save('estadisticas_jefes.xlsx')
