#!/usr/bin/env python3

################################################################################
# SISTEMA DE TESTS CLIENTE-SERVIDOR
# ------------------------------------------------------------------------------
# DESCRIPCIÓN:

# Sistema que permite crear y responder a tests, y consultar los resultados
# de los mismos.
#
# El usuario puede tener dos roles:
# - Administrador: puede crear tests, responderlos y consultar las
#   calificaciones de todos los usuarios.
#
# - Ususario: puede responder tests, y consultar sus propias calificaciones.
#
# ------------------------------------------------------------------------------
# ESTRUCTURA:
# La estructura del sistema completo se halla en la memoria entregada junto
# con este software.
#
# ------------------------------------------------------------------------------


################################################################################

import socket
import sqlite3

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

conn_db = sqlite3.connect('formulario.db')
c = conn_db.cursor()

class Usuario:
    nombre = None;
    ip = None;
    logged = None;
    is_admin = False;

    def __eq__(self, other):
        return self.nombre == other.nombre

usuarios = []

def user_exists(nombre):
    for u in usuarios:
        if nombre == u.nombre:
            return True
    return False

def check_pass(user, password):
    c.execute("SELECT password FROM Usuarios WHERE user=\'%s\'" % user)
    if c.fetchone()[0] == password:
        return True
    return False

def check_is_admin(user):
    c.execute("SELECT password FROM Usuarios WHERE user=\'%s\'" % user)
    if c.fetchone()[0] == '1':
        return True
    return False

def get_user(addr):
    for x in usuarios:
        if x.ip == addr:
            return True
    return False

def check_form_exists(nombre):
    c.execute("SELECT * FROM Formularios WHERE nombre=\'%s\'" % nombre)
    if c.fetchone() is None:
        return True
    return False

def crear_formulario(nombre):
    if not check_form_exists(nombre):
        c.execute('INSERT into Formularios values(?,null,null,null,null,null)', (nombre))
        return True
    return False

def add_question(nombre, pregunta):
    c.execute("SELECT * FROM Formularios WHERE nombre=\'%s\'" % nombre)
    indice = 1
    if c.fetchone()[2] is "null":
        break
    if c.fetchone()[3] is "null":
        indice = 2
        break
    if c.fetchone()[4] is "null":
        indice = 3
        break
    if c.fetchone()[5] is "null":
        indice = 4
        break
    indice = 'pregunta' + str(indice)
    if not check_form_exists(nombre):
        c.execute('UPDATE into Formularios SET %s=%s' % indice, pregunta)
        return True
    return False

def check_question_exists(nombre, pregunta):
    c.execute("SELECT * FROM Formularios WHERE nombre=\'%s\'" % nombre)
    if c.fetchone()[2] == pregunta:
        return True
    if c.fetchone()[3] == pregunta:
        return True
    if c.fetchone()[4] == pregunta:
        return True
    if c.fetchone()[5] == pregunta:
        return True
    return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).split(';')
            if not data:
                break
            else:
                if data[0] == 'LOGIN':
                    if check_pass(data[1], data[2]):
                        if not user_exists(data[1]):
                            usuarios.append(Usuario(nombre=data[1], ip=addr, logged=True, is_admin=check_is_admin(data[1], data[2])))
                    else:
                        if usuario.is_admin:
                            conn.sendall(b'OK;ADMIN')
                        else:
                            conn.sendall(b'OK;USER')

                if data[0] == 'MENU':
                    if get_user(addr).logged:
                        if get_user(addr).is_admin:
                            conn.sendall(b'Crear formulario;Rellenar formulario;Consultar notas')
                        else:
                            conn.sendall(b'Rellenar formulario;Consultar notas')

                if data[0] == 'CREAR_FORMULARIO':
                    if get_user(addr).logged and get_user(addr).is_admin:
                        if crear_formulario(data[1]):
                            conn.sendall(b'OK')
                        else:
                            conn.sendall(b'ERR')

                if data[0] == 'ADD_QUESTION':
                    if get_user(addr).logged and get_user(addr).is_admin and check_form_exists(data[1]):
                        add_question(data[2])
                        conn.sendall(b'OK')
                    else:
                        conn.sendall(b'ERR')

                if data[0] == 'ADD_ANSWER':
                    if get_user(addr).logged and get_user(addr).is_admin and check_question_exists(data[1], data[2]):
                        add_answer(data[1], data[2])
                        conn.sendall(b'OK')
                    else:
                        conn.sendall(b'ERR')
