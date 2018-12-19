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

def login():
	# Establecemos el tipo de paquete que queremos enviar:
	pack = 'LOGIN;'

	# Preguntamos al usuario:
	user = input('Introduzca su usuario: ')
	passwd = input('Introduzca su contraseña: ')

	# Vamos añadiendo el contenido del paquete:
	message = ';'.join(pack, user, passwd)

	# Enviamos el mensaje al servidor:
	s.send(message)

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

		# Pasamos al menú:
		menu()
	else:
		print("Error de autenticación.")
		exit()

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
	for i in range(0, len(data)):
		print("{}: {}\n".format(i, data[i-1]))

	# El usuario selecciona una opción del menú:
	option = input("Selecciona una opción con su número correspondiente: ")

	if option not in range(1, len(data)):
		print("Opción no disponible.")
		exit()

	elif 'Crear' in data[option-1]:
		crear()

	elif 'Salir' in data[option-1]:
		s.close()
		exit()

	else:
		print('Opción no implementada.')
		exit()


def crear():
	# Enviamos la petición de crear cuestionario
	pack = 'CREAR_FORMULARIO'

	# Pedimos al usuario el nombre del formulario:
	name = input("Por favor, introduzca el nombre del formulario: ")

	# Componemos el mensaje a enviar:
	message = ';'.join(pack, name)

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

	# Pedimos al usuario que introduzca una pregunta:
	pregunta = input('Introduce una pregunta. Para volver al menú, no pongas nada: ')

	if pregunta == '':
		menu()

	# Elaboramos el mensaje:
	message = ';'.join(pack, pregunta)

	# Enviamos el mensaje al servidor:
	s.send(message)

	# Recibimos datos del servidor:
	aux = s.recv(BUFFER_SIZE)

	# Interpretamos el formato del paquete:
	data = aux.split(';')

	# Comprobamos si se puede crear:
	if data[0] is 'OK':
		add_answer()

	else:
		print("Opción no permitida.")
		exit()

def add_answer():
	# Enviamos la petición de crear cuestionario
	pack = 'ADD_ANSWER'
	respuesta = []

	# Pedimos al usuario que introduzca la respuesta correcta:
	respuesta[0] = input('Introduce la respuesta correcta: ')

	# Introducimos tres respuestas falsas:
	for i in range(1,3):
		respuesta[i] = input('Introduce una respuesta falsa: ')

	# Elaboramos el mensaje:
	message = ';'.join(pack, respuesta)

	# Enviamos el mensaje al servidor:
	s.send(message)

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


def main():
	s.connect((HOST, PORT))
	login()

if __name__ == '__main__':
	main()
