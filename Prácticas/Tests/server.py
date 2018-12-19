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

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

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

#Sin implementar
def check_pass(user, pass):
    return

#Sin implementar
def check_is_admin(user):
    return

#Sin implementar
def get_user(addr):
    return

#Sin implementar
def check_form_exists(nombre):
    return

#Sin implementar
def crear_formulario(nombre):
    return

#Sin implementar
def add_question(nombre):
    return

#Sin implementar
def check_question_exists(nombre, pregunta):
    return

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

            conn.sendall(data)
