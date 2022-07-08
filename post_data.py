# El proyecto debe contener lo siguiente:
# 1. Caso escrito que describa con detalle el problema, la necesidad y los requisitos lógicos
# a considerar.
# 2. Modelo Entidad Relación con, al menos, 6 entidades (fuertes o débiles) en total.
# # 3. Script de Python que carga los datos con instrucción INSERT INTO en 4 de las 6 tablas creadas.


# Respuestas
# 1.
# Caso escrito:
# # Somos una startup que ofrece exámenes médicos a domicilio. A nuestros clientes les ofrecemos la posibilidad de programar una cita con uno de nuestros médicos a domicilio, en la que se les realizarán una serie de exámenes médicos. Nuestros clientes son personas que no pueden o no quieren acudir a una clínica para realizarse estos exámenes.
# # Nuestros médicos a domicilio se encargarán de ir a la casa del cliente a la hora acordada, realizarle los exámenes médicos que este haya solicitado y luego enviar los resultados a nuestra clínica. Los resultados de los exámenes se almacenarán en nuestra base de datos, para que nuestros clientes puedan consultarlos en cualquier momento.


# 2.
# Modelo ER:
# Nuestro modelo ER tiene 6 entidades:
# - Cliente (nombre, ubicación, horario)
# - Médico (nombre, área de medicina, horario)
# - Examen (nombre, resultado, laboratorio)
# - Cita (cliente, médico, examen, fecha, hora)
# - Isapre (nombre, cobertura)
# - Clínica (nombre, ubicación, horario)


# 3.
import sqlite3
import csv
import os
import sys
import time


def post_data():
    # Crear base de datos
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()

    # Crear tablas
    c.execute(
        """CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        ubicacion TEXT,
        horario TEXT
    )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS medico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        area_medica TEXT,
        horario TEXT
    )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS examen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        resultado TEXT,
        laboratorio TEXT
    )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS cita (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        medico_id INTEGER,
        examen_id INTEGER,
        fecha TEXT,
        hora TEXT
    )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS isapre (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        cobertura TEXT
    )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS clinica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        ubicacion TEXT,
        horario TEXT
    )"""
    )

    # Cargar datos
    c.execute(
        """INSERT INTO cliente (nombre, ubicacion, horario) VALUES ('Juan', 'Calle falsa 123', '8:00 a.m. a 9:00 p.m.')"""
    )
    c.execute(
        """INSERT INTO cliente (nombre, ubicacion, horario) VALUES ('Ped¿', 'Calle falsa 123', '8:00 a.m. a 9:00 p.m.')"""
    )

    return conn, c

def create_random_data(conn, c):
    # primero, crea un generador de nombres random
    nombres = ["Juan", "Pedro", "María", "José", "Pablo", "Miguel", "Juan", "Pedro", "María", "José", "Pablo", "Miguel", "daniel",