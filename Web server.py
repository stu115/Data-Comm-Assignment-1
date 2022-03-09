# Import socket module
from socket import *    

# A TCP server socket is made
#(AF_INET is being used for version 4 of the format for running the Internet i.e.(IPv4) protocols)
#(Use SOCK_STREAM is d for the format for transferring files i.e. TCP)

socketOnServer = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket and a port number for the server.

portOnServer = 6789

# Join i.e.bind the server socket to the server port
socketOnServer.bind(("", portOnServer))

# Server socket starts listening which means it is ready to receive a connection which is in a queue 
# as many as 1
socketOnServer.listen(1)

# Fill in end
while True: 
	print('Can serve now...')
	# Get the connection ready
	# Create a connection to the client through a connection socket
	socketThatConnects, addr = socketOnServer.accept()
	
	try:
		# Read the request sent by the client at the connection socket
		message =  socketThatConnects.recv(1024)
		# Split the message received at the connection socket and decode it
	        filename = message.split()[1]
		# The extracted path of the HTTP request has  a character '\'. We read the path from the character that's next 
		f = open(filename[1:].decode())
                databeingoutput = f.read()
		# Start sending a reply to the clients request
		socketThatConnects.send("HTTP/1.1 200 OK\r\n\r\n".encode())
 
		# Pass what is in the requested file to the connection socket  
		for i in range(0, len(databeingoutput)):  
			socketThatConnects.send(databeingoutput[i].encode())
		socketThatConnects.send("\r\n".encode())
		
		# Close the socket that connects to the client
		socketThatConnects.close()

	except IOError:
		# #Send a response message if the file is not held by the serve
		socketThatConnects.send("HTTP/1.1 404 Does not seem to be there\r\n\r\n".encode())
		socketThatConnects.send("<html><head></head><body><h1>404 Does not seem to be there</h1></body></html>\r\n".encode())
		# Close the socket that connects to the client
		socketThatConnects.close()

socketOnServer.close()  

