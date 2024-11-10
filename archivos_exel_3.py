import pandas as pd
# Leer un archivo de Excel
df = pd.read_excel('estadisticas_jefes.xlsx', sheet_name='Estadísticas Jefes')
print(df)
# Escribir datos en un archivo Excel
df_nuevo = pd.DataFrame({
    'Jefe': ['Manus', 'Kalameet'],
    'Vida': [7000, 5500],
    'Localización': ['Abyss', 'Oolacile']
})
df_nuevo.to_excel('nuevas_estadisticas.xlsx', index=False)
