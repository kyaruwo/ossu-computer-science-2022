import socket

#create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect my socket to the pr4e socket
mysock.connect(("data.pr4e.org", 80))
#create a command
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
#send the command
mysock.send(cmd)

while True:
    #receive data from the socket by 512 bytes and store it in a variable
    data = mysock.recv(512)
    if (len(data) < 1):
        #break if there is no more data to be receive
        break
    else:
        #print the data that has been receive
        print(data.decode())
mysock.close()