# Proyecto Semestral 2022-I

## Respuestas a las preguntas 1 y 2
#### 1. Caso escrito:

Somos una startup que ofrece exámenes médicos a domicilio. A nuestros clientes les ofrecemos la posibilidad de programar una cita con uno de nuestros médicos a domicilio, en la que se les realizarán una serie de exámenes médicos. Nuestros clientes son personas que no pueden o no quieren acudir a una clínica para realizarse estos exámenes.

Nuestros médicos a domicilio se encargarán de ir a la casa del cliente a la hora acordada, realizarle los exámenes médicos que este haya solicitado y luego enviar los resultados a nuestra clínica. Los resultados de los exámenes se almacenarán en nuestra base de datos, para que nuestros clientes puedan consultarlos en cualquier momento.

#### 2. Modelo ER:
Nuestro modelo ER tiene 6 entidades:
- Cliente (nombre, ubicación, horario)
- Médico (nombre, área de medicina, horario)
- Examen (nombre, resultado, laboratorio)
- Cita (cliente, médico, examen, fecha, hora)
- Isapre (nombre, cobertura)
- Clínica (nombre, ubicación, horario)

## Contexto

Objetivo: El objetivo del proyecto es que el estudiante experimente el proceso completo desde
el diseño hasta la extracción de datos de una base de datos, entendiendo el uso que se le puede
dar a la herramienta en un contexto real.

El trabajo debe ser desarrollado en grupos de máximo 4 integrantes.

Este proyecto consiste en buscar y definir un caso “real”, que refleje algún proceso de negocio
en alguna organización de las siguientes industrias o actividades:
- Educación
- Salud
- Turismo
- Minería
- Agricultura

### El proyecto debe contener lo siguiente
1. Caso escrito que describa con detalle el problema, la necesidad y los requisitos lógicos
a considerar.
2. Modelo Entidad Relación con, al menos, 6 entidades (fuertes o débiles) en total.
3. Modelo lógico.
4. Script SQL con instrucciones DDL del Modelo físico validado en tercera forma normal.
5. Script de Python que carga los datos con instrucción INSERT INTO en 4 de las 6 tablas
creadas.
6. Script de Python que rescate la información desde archivos CSVs y la cargue en las 2
tablas definidas para este tipo de carga de datos.
7. Script Python con 12 consultas SQL basadas en el modelo que permitan contestar
preguntas relevantes del caso. Considere los siguientes tipos de consultas:

    a. 4 consultas simples a 4 tablas específicas.

    b. 4 consultas que contengas JOIN entre tablas.

    c   . 4 consultas que agrupen información, contando registros, sumando valores de
algún campo específico, sacando promedios de valores de algún campo
específico.

Tienes que entregar tus informes con todos tus análisis, supuestos y descripciones (ver
formato detallado más abajo) de la forma más profesional posible. Piensa que esto lo
debería leer un ejecutivo de la empresa que te ha encargado este desarrollo.

### Entregables
1. Power Point con los temas 1, 2, 3 desarrollados y explicados.
2. Script SQL para el punto 4. Este Script SQL debe poder ejecutarse en Workbench, crear
la base de datos y las tablas en Mysql Xampp en cualquier equipo con Windows en el
que corra.
3. Notebooks python con los temas 5, 6, 7. Estos Notebooks deben poder ejecutarse sin
errores en Jupyter Notebooks conectado a la Base de datos en Mysql Xampp.
