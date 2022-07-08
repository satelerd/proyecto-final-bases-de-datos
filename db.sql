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
