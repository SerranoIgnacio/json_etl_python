# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
from uuid import uuid5
import requests
import matplotlib.pyplot as plt
from sqlalchemy import true


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    u = []
    u1=0 
    u2=0 
    u3=0 
    u4=0
    u5=0
    u6=0
    u7=0
    u8=0
    u9=0
    u10=0

    for user in data:
        if user['completed'] == True:
            #print('El usuario {} completó {}'.format(user['userId'], user['title']))
            if user['userId'] == 1:
                u1 = u1 + 1
            elif user['userId'] == 2:
                u2 = u2 + 1
            elif user['userId'] == 3:
                u3 = u3 + 1
            elif user['userId'] == 4:
                u4 = u4 + 1
            elif user['userId'] == 5:
                u5 = u5 + 1
            elif user['userId'] == 6:
                u6 = u6 + 1
            elif user['userId'] == 7:
                u7 = u7 + 1
            elif user['userId'] == 8:
                u8 = u8 + 1
            elif user['userId'] == 9:
                u9 = u9 + 1
            elif user['userId'] == 10:
                u10 = u10 + 1
    u = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
    ca = [1,2,3,4,5,6,7,8,9,10]
    print(u)

    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    fig = plt.figure()      # Definir tamaño figura
    ax = fig.add_subplot() # Definir cuantos gráficos tendrá

    ax.bar(ca, u, label='Grafico')           
    ax.set_facecolor('whitesmoke')
    ax.set_title("Cantidad de Titulos completados")
    ax.set_ylabel("Cantidad de Titulos")
    ax.set_xlabel("Id de Alumnos")
    plt.show()              # Mostrar el gráfico

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    print("terminamos")