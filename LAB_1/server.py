import socket
import os
import sockethelp
import mimetypes

#----------------------------------------Server Constant Definitions----------------------------------------
HOST = "localhost"               # Sets the current computer name as hostname
PORT = 1337                      # low number ports are usually reserved, use a nice high number (4 digits) https://docs.python.org/3.5/howto/sockets.html
TIMEOUT = 1                      # Set timeout to 1 second so accept() will become (somewhat nonblocking)
MAX_REQUEST = 1                  # Prepared to listen to a single socket at most
#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # AF_INET corresponds to IPV4 sockets
    # SOCK_STREAM corresponds to TCP 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))
    server_socket.settimeout(TIMEOUT) 
    # Socket is simply an endpoint that send/receives data.
    # It sits in a corresponding port-IP pair
    server_socket.listen(MAX_REQUEST)
    print("Server started: ", HOST, ":", PORT)

    try:
        while True:
            # create connection socket, address -> IP address of where data coming from
            try:
                client_socket, address = server_socket.accept() # Note that accept here is blocking 
                client_message = sockethelp.read_http_header(client_socket) # Receive client HTTP request
                # Parses filename from GET request ie: GET /{filename} HTTP/1.1
                filename = client_message.split()[1][1:] 
                
                # assumption: files are all in same directory as server
                filewithDir = os.path.join(os.path.dirname(__file__), filename)
                
                if os.path.isfile(filewithDir):
                    server_message = "HTTP/1.1 200 OK\n"
                    
                    # Read file content from requested filename
                    file_obj = open(filewithDir, "rb")
                    file_content = file_obj.read()
                    file_obj.close()

                    # Gets the appropriate Content-Type based on file extension
                    content_type = mimetypes.guess_type(filewithDir, strict=True)[0] # This returns a tuple (type, encoding)
                    content_length = str(len(file_content))
                    # Concatenate Content-Type header to HTTP response
                    server_message = server_message + "Content-Type: " + content_type + "\n"
                    # Concatenate Content-Length header to HTTP response
                    server_message = server_message + "Content-Length: " + content_length + "\n"
                    
                    # Send header followed by body
                    sockethelp.write_http_header(client_socket, server_message)

                    # Recieves an ACK message
                    ack = sockethelp.read_http_header(client_socket)

                    # check for ack and send content
                    if ack == "1":

                        # Send content after recieving ACK message
                        sockethelp.write_http_body(client_socket, file_content)

                else:
                    server_message = "HTTP/1.1 404 Not Found"
                    sockethelp.write_http_header(client_socket, server_message)

            except socket.timeout:
                pass

    except KeyboardInterrupt:
        server_socket.close()