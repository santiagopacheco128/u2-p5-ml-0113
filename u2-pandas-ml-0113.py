import numpy as np 
import pandas as pd
# santiago pacheco 0113
## datos matriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print("----------- datos a partir de una matrix 4x3 -------------")
df=pd.DataFrame(datos_alumno,columns=["ci","marcas","paquete"])
print(df)
# datos de apartir de un diccionario
print("-------------datos a partir de una matrix 4x3-------------")
alumno_diccionario={
    "nombre":["Eliseo","Hugo","Nahum","Iker","Jesse"],
    "califa":[60,90,100,80,70],
    "edad":[64,15,16,16,18]
}

estudiante = pd.DataFrame(alumno_diccionario)
print(estudiante)
print("Santiago Pacheco NC 0113")