import sqlite3
import csv


def post_data():
    # Crear base de datos
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()

    # Subimos los datos a la base de datos
    with open("clientes.csv", "r") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # Cliente
            c.execute(
                "INSERT INTO cliente (nombre, ubicacion, horario) VALUES (nombre, ubicacion, horario)",
                row,
            )
            # Médico
            c.execute(
                "INSERT INTO medico (nombre, area_medica, horario) VALUES (nombre, area_medica, horario)",
                row,
            )
            # Examen
            c.execute(
                "INSERT INTO examen (nombre, resultado, laboratorio) VALUES (nombre, resultado, laboratorio)",
                row,
            )
            # Cita
            c.execute(
                "INSERT INTO cita (cliente, medico, examen, fecha, hora) VALUES (cliente, medico, examen, fecha, hora)",
                row,
            )
            # Isapre
            c.execute(
                "INSERT INTO isapre (nombre, cobertura) VALUES (nombre, cobertura)", row
            )
            # Clínica
            c.execute(
                "INSERT INTO clinica (nombre, ubicacion, horario) VALUES (nombre, ubicacion, horario)",
                row,
            )

    conn.commit()
    conn.close()

    print("Datos cargados correctamente")
    return


# 4.
def consultas_sql():
    # Crear base de datos
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()

    # Consultas SQL
    # a. 4 consultas simples a 4 tablas específicas.
    # 1. Cliente
    c.execute("SELECT * FROM cliente WHERE ubicacion = 'Ciudad' AND horario = 'Mañana'")
    print("1. Cliente")
    print(c.fetchall())
    print("---------------------------------------------")
    # 2. Médico
    c.execute(
        "SELECT * FROM medico WHERE area_medica = 'Cardiología' AND horario = 'Mañana'"
    )
    print("2. Médico")
    print(c.fetchall())
    print("---------------------------------------------")
    # 3. Examen
    c.execute(
        "SELECT * FROM examen WHERE laboratorio = 'Laboratorio 1' AND resultado = 'Positivo'"
    )
    print("3. Examen")
    print(c.fetchall())
    print("---------------------------------------------")
    # 4. Cita
    c.execute(
        "SELECT * FROM cita WHERE cliente = 'Juan' AND medico = 'Juan' AND examen = 'Examen 1' AND fecha = '2020-01-01' AND hora = '10:00'"
    )
    print("4. Cita")
    print(c.fetchall())
    print("---------------------------------------------")

    # b. 4 consultas que contengas JOIN entre tablas.
    # 5. Cliente
    c.execute("SELECT * FROM cliente JOIN cita ON cliente.nombre = cita.cliente")
    print("---------------------------------------------")
    print("1. Cliente")
    print(c.fetchall())
    print("---------------------------------------------")
    # 6. Médico
    c.execute("SELECT * FROM medico JOIN cita ON medico.nombre = cita.medico")
    print("2. Médico")
    print(c.fetchall())
    print("---------------------------------------------")
    # 7. Examen
    c.execute("SELECT * FROM examen JOIN cita ON examen.nombre = cita.examen")
    print("3. Examen")
    print(c.fetchall())
    print("---------------------------------------------")
    # 8. Clínica
    c.execute("SELECT * FROM clinica JOIN cita ON clinica.nombre = cita.clinica")
    print("4. Clínica")
    print(c.fetchall())
    print("---------------------------------------------")

    # c. 4 consultas que agrupen información, contando registros, sumando valores de algún campo específico, sacando promedios de valores de algún campo específico.
    # 9. Cliente
    c.execute(
        "SELECT COUNT(*) FROM cliente WHERE ubicacion = 'Ciudad' AND horario = 'Mañana'"
    )
    print("---------------------------------------------")
    print("1. Cliente")
    print(c.fetchall())
    print("---------------------------------------------")
    # 10. Médico
    c.execute(
        "SELECT COUNT(*) FROM medico WHERE area_medica = 'Cardiología' AND horario = 'Mañana'"
    )
    print("2. Médico")
    print(c.fetchall())
    print("---------------------------------------------")
    # 11. Examen
    c.execute(
        "SELECT COUNT(*) FROM examen WHERE laboratorio = 'Laboratorio 1' AND resultado = 'Positivo'"
    )
    print("3. Examen")
    print(c.fetchall())
    print("---------------------------------------------")
    # 12. Cita
    c.execute(
        "SELECT COUNT(*) FROM cita WHERE cliente = 'Juan' AND medico = 'Juan' AND examen = 'Examen 1' AND fecha = '2020-01-01' AND hora = '10:00'"
    )
    print("4. Cita")
    print(c.fetchall())
    print("---------------------------------------------")

    conn.commit()
    conn.close()

    return
