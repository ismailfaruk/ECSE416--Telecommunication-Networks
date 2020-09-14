import socket
import os
import sockethelp
#----------------------------------------Server Definitions----------------------------------------
# Server Definitions
Host = socket.gethostname()     # Sets the current computer name as hostname
Port = 1337                     # low number ports are usually reserved, use a nice high number (4 digits) https://docs.python.org/3.5/howto/sockets.html
Timeout = 1                     # Set timeout to 1 second so accept() will become (somewhat nonblocking)
MaxRequest = 1                  # Prepared to listen to a single socket at most
BufferSize = 1024               # MAX of 1024 bytes for the buffer
#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # AF_INET corresponds to IPV4 sockets
    # SOCK_STREAM corresponds to TCP 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # socket.gethosename makes socket visible to outside world.
    server_socket.bind((Host, Port))
    server_socket.settimeout(Timeout) 
    # Socket is simply an endpoint that send/receives data.
    # It sits in a corresponding port-IP pair
    server_socket.listen(MaxRequest)
    print("Server started: ", Host, ":", Port)

    try:
        while True:
            # create connection socket, address -> IP address of where data coming from
            try:
                client_socket, address = server_socket.accept() # Note that accept here is blocking 
                # Remember sockets receive stream of data ( how much chunks of data we receive at a time)
                ClientMessage = sockethelp.read(client_socket)
                print(ClientMessage)

                if os.path.isfile(ClientMessage):
                    ServerMessage = "HTTP/1.1 200 OK"                    
                else:
                    ServerMessage = "\HTTP/1.1 404 not found"
                
                sockethelp.write(client_socket, ServerMessage)
            
            except socket.timeout:
                pass

            # TODO
            # 1. Receive an HTTP request
            # 2. Parse it to retrieve filename
            # 3. Get file from directory
            # 4. Send HTTP response to client with file content (404 if file not found)

    except KeyboardInterrupt:
        server_socket.close()