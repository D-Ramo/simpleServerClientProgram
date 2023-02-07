import socket
import sys
import socket
import selectors
import types
    
HOST = socket.gethostname() # The server's hostname or IP address
PORT = 5000 # The port used by the server


def numOfOccurance(key, String): #function to find number of occurances in a string
    num=0
    for char in String:
        if(char == key):
            num+=1
    return num



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #here we are initializing the socket using internet adress family IPv4
    s.bind((HOST, PORT)) #creates a socket server with the given host and port  
    s.listen(1) #listenes to clients for connection

    conn, adr = s.accept() # blocks execution and waits for an incoming connection.
    with conn:
        print(f"connected by {adr}")
        while True:
            #get inputs from client
            Char = conn.recv(1024).decode() 
            String = conn.recv(1024).decode()
            
            numOfOccurences= numOfOccurance(Char,String) #get num of occurences
            conn.send(str.encode(str(numOfOccurences))) #send result to client to be printed
