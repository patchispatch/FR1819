# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('formulario.db')

c = conn.cursor()

consulta = '''
CREATE TABLE `Usuarios` (
  `user` TEXT NOT NULL,
  `password` TEXT NOT NULL,
  `is_admin` TEXT NOT NULL DEFAULT 0,
  PRIMARY KEY (`user`));

CREATE TABLE `Formularios` (
  `nombre` TEXT NOT NULL,
  `pregunta` TEXT NULL,
  `respuesta1` TEXT NULL,
  `respuesta2` TEXT NULL,
  `respuesta3` TEXT NULL,
  `respuesta4` TEXT NULL,
  PRIMARY KEY (`nombre`));

INSERT INTO Usuarios VALUES ('jose','pene','1');
'''

c.execute(consulta)

conn.commit()
conn.close()
