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

El Sistema pide que ingresemos el Numero de Identificacion para poder consultar al estudiante

```
Ingrese el numero de identificacion: 1041

Nombre: Marcos
Edad: 17
Notas: [4.0, 5.0, 3.5]
Promedio: 4.17
```

## En el caso de seleccionar la funcion #3 (Actualizar notas)

El sistema pide que ingresemos nuevamente el Numero de Identifiacion pero esta vez para poder actualizar la nota de un estudiante en especifico

```
Selecciona una opción (1-6): 3
Ingrese el numero de identificacion: 1041
Nota nueva 1 (0 a 5): 5
Nota nueva 2 (0 a 5): 1
Nota nueva 3 (0 a 5): 5
Notas actualizadas para Marcos

```

## En el caso de seleccionar la funcion #4 (Eliminar estudiante)

El sistema pide que ingresemos el Numero de Identifiacion para poder aleminir al estudiante seleccionado

```
Selecciona una opción (1-6): 4
Ingrese el numero de identificación del estudiante a eliminar: 1041
Estudiante Marcos eliminado con exito.

```

## En el caso de seleccionar la funcion #5 (Eliminar estudiante)

El sistema pide que ingresemos el digito en este caso "5" y nos dara 

```
Selecciona una opción (1-6): 5

Lista de todos los estudiantes:

ID: 1041 | Nombre: Maria | Edad: 5 | Promedio: 5.00

ID: 1042 | Nombre: Daniel | Edad: 18 | Promedio: 2.93

ID: 1043 | Nombre: Andres | Edad: 1 | Promedio: 1.00

```


## En el caso de seleccionar la funcion #6 (SALIR)

Con esta opcion el sistema se cierra

```
Selecciona una opción (1-6): 6
Finalizando programa...
```


## Construido con 🛠️

-Python
https://docs.python.org/es/3/
https://github.com/Riwi-io-Medellin/Python_Fundamentals


