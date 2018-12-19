################################################################################
# SISTEMA DE TESTS CLIENTE-SERVIDOR
# ------------------------------------------------------------------------------
# DESCRIPCIÓN:
#
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
# AUTORÍA:
# Este software ha sido realizado por José Baena Cobos y Juan Ocaña Valenzuela,
# estudiantes de Fundamentos de Redes en el curso 2018-2019.
#
# ------------------------------------------------------------------------------
# LICENCIA:
#
################################################################################

# Importamos la biblioteca de socket de Python:
import socket

# Detalles de la conexión:
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

# Socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Métodos:

def login(user, passwd):
	# Establecemos el tipo de paquete que queremos enviar:
	pack = 'LOGIN;'

	# Vamos añadiendo el contenido del paquete:
	pack.join(user.join(';'.join(passwd)))

	# Enviamos el mensaje al servidor:
	s.send(pack)

	# Recibimos datos del servidor:
	aux = s.recv(BUFFER_SIZE)

	# Interpretamos el formato del paquete:
	data = aux.split(';')

	# Comprobamos si el login ha sido exitoso:
	if data[0] == 'OK':
		print('Login correcto.\n')

		# Actualizamos el tipo de usuario:
		if data[1] == 'USER':
			print('Usted es usuario.')
		elif data[1] == 'ADMIN':
			print('Usted es administrador.')
	else:
		print("Error de autenticación.")

def menu():
	# Establecemos el tipo de paquete que queremos enviar:
	pack = 'MENU'

	# Enviamos el mensaje al servidor:
	s.send(pack)

	# Recibimos datos del servidor:
	aux = s.recv(BUFFER_SIZE)

	# Interpretamos el formato del paquete:
	data = aux.split(';')

	# Imprimimos las opciones del menú recibidas:
	for i in range(0, len(data):
		print("{}: {}\n".format(i, data[i-1])

	# El usuario selecciona una opción del menú:
	option = input("Selecciona una opción con su número correspondiente: ")

	if option not in range(1, len(data)):
		print("Opción no disponible.")
		exit()

	elif 'Crear' in data[option]:
		crear()


def crear():
	# Enviamos la petición de crear cuestionario
	pack = 'CREAR_FORMULARIO'

	# Enviamos el mensaje al servidor:
	s.send(pack)

	# Recibimos datos del servidor:
	aux = s.recv(BUFFER_SIZE)

	# Interpretamos el formato del paquete:
	data = aux.split(';')

	# Comprobamos si se puede crear:
	if data[0] is 'OK':
		add_question()

	else:
		print("Opción no permitida.")
		exit()

def add_question():
	# Enviamos la petición de añadir pregunta:
	pack = 'ADD_QUESTION'

	# Enviamos el mensaje al servidor:
	s.send(pack)

	# Recibimos datos del servidor:
	aux = s.recv(BUFFER_SIZE)

	# Interpretamos el formato del paquete:
	data = aux.split(';')

	# Comprobamos si se puede añadir:
	if data[0] is 'OK':
		question = input('Introduce una pregunta: ')
		send_question(question)

	else:
		print("Opción no permitida.")
		exit()

def send_question():
	# Enviamos la petición de crear cuestionario
	pack = 'ADD_QUESTION'

	# Comprobamos si se puede añadir:
	if data[0] is 'OK':
		question = input('Introduce una pregunta: ')

	else:
		print("Opción no permitida.")
		exit()

	# Enviamos el mensaje al servidor:
	s.send(pack)

	# Recibimos datos del servidor:
	aux = s.recv(BUFFER_SIZE)
