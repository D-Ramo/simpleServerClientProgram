import socket

def readChar(): # this function reads charecters and checks if input is correct or not
    while(True):
        char = input("Enter a Character to be searched: ")
        if ((len(char) > 1) or (len(char)==0)):
            print("Please eneter a Charecter")
            continue
        else: return char

def readString(): # this funciton reads the String and checks if any empty input is entered
    while(True):
        string = input("Enter a String: ")
        if(len(string)== 0):
            print("Please eneter a String ")
            continue
        else: return string

def terminate(): #this checks if the program needs to be terminated by only taking "Y" and "N"
    while(True):
        yesOrNo = input("Want to repeat (Y/N): ") 
        if(yesOrNo == "N" or yesOrNo == "Y" ):
            return yesOrNo 
        else: continue



HOST = socket.gethostname()  # The server's hostname or IP address
PORT = 5000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   #here we are initializing the socket using internet adress family IPv4
    s.connect((HOST, PORT)) #connects to server using both host and port
    
    while True:
        # read the inputs 
        char = readChar()
        string = readString()

        #send the inputs to the server
        s.send(char.encode())
        s.send(string.encode())
       
        recieve = s.recv(1024).decode() #recieve the responce (number of occurences) from the server
        print(f"The number of Occurrences are: {recieve}") #print result
        if terminate() == "N": #if user doesnt want to continue terminate program
            break
print("Thank you!")


