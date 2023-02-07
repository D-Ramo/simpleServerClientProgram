import socket

def readChar():
    while(True):
        char = input("Enter a Character to be searched: ")
        if ((len(char) > 1) or (len(char)==0)):
            print("Please eneter a Charecter")
            continue
        else: return char

def readString():
    while(True):
        string = input("Enter a String: ")
        if(len(string)== 0):
            print("Please eneter a String ")
            continue
        else: return string

def terminate():
    while(True):
        yesOrNo = input("Want to repeat (Y/N): ") 
        if(yesOrNo == "N" or yesOrNo == "Y" ):
            return yesOrNo 
        else: continue



HOST = socket.gethostname()  # The server's hostname or IP address
PORT = 5000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        char = readChar()
        string = readString()

        s.send(char.encode())
        s.send(string.encode())

        recieve = s.recv(1024).decode()
        print(f"The number of Occurrences are: {recieve}")
        if terminate() == "N":
            break
print("Thank you!")


