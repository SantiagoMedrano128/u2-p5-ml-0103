import numpy as np 
import pandas as pd
# Santiago Medrano NC 0103
 ## datos matriz 4 x 3
datos_alumnos = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
#poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print("-------- Datos a partir de una matriz de 4 x 3 --------")
df=pd.DataFrame(datos_alumnos,columns=['ci','marcas','paquete'])
print(df)
#datos a partor de un diccionario
print("-------- Datos a partir de un diccionario --------")
alumno_diccionario={
    "nombre":["Eliseo", "Joel", "Pedro", "Nicole", "Dilan", " Jesse"],
    "califa":[60,90,100,80,70,50],
    "edad":[64,15,16,16,18,14]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Santiago Medrano NC 0103")