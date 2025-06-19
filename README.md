# Gestión de estudiantes

Es un programa escrito en Python que permite gestionar la información académica de estudiantes usando variables, condicionales, ciclos
(while y for), listas y diccionarios, y su objetivo como tal es que administre los registros académicos de
estudiantes, aplicando correctamente las estructuras de control y tipos de datos.



### Funciones

El codigo Consta de 6 funciones las cuales son:

1. Registrar estudiante
2. Consultar estudiante
3. Actualizar notas
4. Eliminar estudiante
5. Ver todos los estudiantes
6. Salir


```
# Menu principal
def mostrar_menu():
    print("MENÚ DE OPCIONES ")
    print("1. Registrar estudiante")
    print("2. Consultar estudiante")
    print("3. Actualizar notas")
    print("4. Eliminar estudiante")
    print("5. Ver todos los estudiantes")
    print("6. Salir")
```

### Como usarlo

Para iniciar el codigo debes ejecutarlo, Luego te dara un mensaje como este:

```
Bienvenido a La Gestión de estudiantes 

                 ／＞　 フ
                | 　_　_|
              ／` ミ＿xノ
             /　　　　 |
            /　 ヽ　　 ﾉ
           │　　|　|　|
        ／￣|　　 |　|　
        (￣ヽ＿_ヽ_)__)
------------------------------
MENÚ DE OPCIONES 
1. Registrar estudiante
2. Consultar estudiante
3. Actualizar notas
4. Eliminar estudiante
5. Ver todos los estudiantes
6. Salir
Selecciona una opción (1-6): 

```

Tendras que digitar un numero del 1 al 6 segun la opcion de la funcion que quieras usar.

## En el caso de seleccionar la funcion #1 (Registrar Estudiante)

te pedira que llenes los campos que son: Numero de identificacion (ID), Nombre del estudiante y Edad.

```
Selecciona una opción (1-6): 1
Numero de identificacion: 1041
Nombre: Marcos
Edad: 17

```

Luego te solicitara 3 Notas para guardar finalmente al estudiante:

```
Ingrese la nota 1 (0 a 5): 4.0
Ingrese la nota 2 (0 a 5): 5
Ingrese la nota 3 (0 a 5): 3.5
Estudiante Marcos registrado.
```

Al finalizar cada funcion le volvera automaticamente al Menu.


## En el caso de seleccionar la funcion #2 (Consultar Estudiante)

_Explica como ejecutar las pruebas automatizadas para este sistema_

```
Ingrese el numero de identificacion: 1041

Nombre: Marcos
Edad: 17
Notas: [4.0, 5.0, 3.5]
Promedio: 4.17
```


### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_


### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

-Python
https://docs.python.org/es/3/
https://github.com/Riwi-io-Medellin/Python_Fundamentals


