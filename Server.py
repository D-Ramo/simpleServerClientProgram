import socket
import sys
import socket
import selectors
import types
    
HOST = socket.gethostname()
PORT = 5000

def numOfOccurance(key, String):
    num=0
    for char in String:
        if(char == key):
            num+=1
    return num



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    conn, adr = s.accept()
    with conn:
        print(f"connected by {adr}")
        while True:
            Char = conn.recv(1024).decode()
            String = conn.recv(1024).decode()
            numOfOccurences= numOfOccurance(Char,String)
            conn.send(str.encode(str(numOfOccurences)))
