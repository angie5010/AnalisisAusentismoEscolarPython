# -*- coding: utf-8 -*-
"""

@author: angie
"""

import pandas as pd
import matplotlib.pyplot as plt
#Cargar los datos
data = pd.read_csv('2018-2019_Daily_Attendance_20240429.csv', delimiter = ',')

print(data.isnull().sum())

print(data.describe())



# Calcular la tasa de asistencia
data['Tasa_Asistencia'] = data['Present'] / data['Enrolled'] * 100
print(data.Tasa_Asistencia)

# Calcular la tasa promedio de asistencia por escuela
tasa_asistencia_promedio = data.groupby('School DBN')['Tasa_Asistencia'].mean().reset_index()
tasa_asistencia_promedio.columns = ['School DBN', 'Tasa_Asistencia_Promedio']
print(tasa_asistencia_promedio)

##Histograma
# Visualizar la distribución de la tasa promedio de asistencia
tasa_asistencia_promedio['Tasa_Asistencia_Promedio'].hist(figsize=(10, 6))
plt.title('Distribución de la Tasa Promedio de Asistencia por Escuela')
plt.xlabel('Tasa de Asistencia Promedio (%)')
plt.ylabel('Frecuencia')
plt.show()



##Grafico pastel

# Calcular totales de Ausente, Presente y Dado de baja
total_ausente = data['Absent'].sum()
total_presente = data['Present'].sum()
total_dado_de_baja = data['Released'].sum()

# Datos para el gráfico de pastel
categorias = ['Ausente', 'Presente', 'Dado de baja']
valores = [total_ausente, total_presente, total_dado_de_baja]


# Crear el gráfico de pastel sin titulo
plt.figure(figsize=(8, 8))
plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
#plt.title('Distribución de Asistencia por Categoría')
plt.axis('equal')  # Para que el gráfico de pastel tenga forma de círculo
plt.show()

##Gráfico de barras
# Calcular el total de estudiantes retirados por escuela
retirados_por_escuela = data.groupby('School DBN')['Released'].sum()

# Graficar el total de estudiantes retirados por escuela
plt.figure(figsize=(10, 6))
retirados_por_escuela.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title('Top 10 Escuelas con Más Estudiantes Retirados')
plt.xlabel('Escuela')
plt.ylabel('Total de Estudiantes Retirados')
plt.xticks(rotation=0)
plt.show()

##Gráfico de barras

# Asegurarte de que la columna 'Date' está en formato datetime
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')

# Agregar una columna 'Month' que represente el mes
data['Month'] = data['Date'].dt.to_period('M')
# Calcular la cantidad de estudiantes ausentes por mes
ausentes_por_mes = data.groupby('Month')['Absent'].sum()

# Graficar la cantidad de estudiantes ausentes por mes
plt.figure(figsize=(10, 6))
ausentes_por_mes.plot(kind='bar')
plt.title('Cantidad de Estudiantes Ausentes por Mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Ausentes')
plt.xticks(rotation=0)
plt.show()

##Gráfico de barras

# Asegurarse de que la columna 'Date' está en formato datetime
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')

# Agregar una columna 'Month' que represente el mes
data['Month'] = data['Date'].dt.to_period('M')

# Filtrar los datos excluyendo el mes de junio de 2019
data_filtrado = data[data['Month'] != '2019-06']

# Calcular la cantidad de estudiantes retirados por mes
retirados_por_mes = data_filtrado.groupby('Month')['Released'].sum()

# Graficar la cantidad de estudiantes retirados por mes
plt.figure(figsize=(12, 6))
retirados_por_mes.plot(kind='bar')
plt.title('Cantidad de Estudiantes Retirados por Mes (Excluyendo Junio 2019)')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Estudiantes Retirados')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', linewidth=0.7)
plt.tight_layout()  # Para ajustar automáticamente el espaciado del gráfico
plt.show()
