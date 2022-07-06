-- ##El proyecto debe contener lo siguiente:
-- 1. Caso escrito que describa con detalle el problema, la necesidad y los requisitos lógicos
-- a considerar.
-- 2. Modelo Entidad Relación con, al menos, 6 entidades (fuertes o débiles) en total.
-- 3. Script SQL con instrucciones DDL del Modelo físico validado en tercera forma .

-- ## Respuestas
-- 1. 
-- Caso escrito:
-- Somos una startup que ofrece exámenes médicos a domicilio. A nuestros clientes les ofrecemos la posibilidad de programar una cita con uno de nuestros médicos a domicilio, en la que se les realizarán una serie de exámenes médicos. Nuestros clientes son personas que no pueden o no quieren acudir a una clínica para realizarse estos exámenes.

-- Nuestros médicos a domicilio se encargarán de ir a la casa del cliente a la hora acordada, realizarle los exámenes médicos que este haya solicitado y luego enviar los resultados a nuestra clínica. Los resultados de los exámenes se almacenarán en nuestra base de datos, para que nuestros clientes puedan consultarlos en cualquier momento.

-- 2. 
-- Modelo ER:
-- Nuestro modelo ER tiene 6 entidades:
-- - Cliente (nombre, ubicación, horario)
-- - Médico (nombre, área de medicina, horario)
-- - Examen (nombre, resultado, laboratorio)
-- - Cita (cliente, médico, examen, fecha, hora)
-- - Isapre (nombre, cobertura)
-- - Clínica (nombre, ubicación, horario)

-- 3.
-- Script SQL:
CREATE DATABASE db;
USE db;

CREATE TABLE Cliente
(
    id_cliente INTEGER NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    horario VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_cliente)
);

CREATE TABLE Medico
(
    id_medico INTEGER NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    area_medica VARCHAR(255) NOT NULL,
    horario VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_medico)
);

CREATE TABLE Examen
(
    id_examen INTEGER NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    resultado VARCHAR(255) NOT NULL,
    laboratorio VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_examen)
);

CREATE TABLE Cita
(
    id_cita INTEGER NOT NULL,
    cliente INTEGER NOT NULL,
    medico INTEGER NOT NULL,
    examen INTEGER NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    PRIMARY KEY (id_cita),
    FOREIGN KEY (cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (medico) REFERENCES Medico(id_medico),
    FOREIGN KEY (examen) REFERENCES Examen(id_examen)
);

CREATE TABLE Isapre
(
    id_isapre INTEGER NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    cobertura VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_isapre)
);
|