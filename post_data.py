#El proyecto debe contener lo siguiente:
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
#copilot