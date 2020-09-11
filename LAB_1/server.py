import socket

# AF_INET corresponds to IPV4 sockets
# SOCK_STREAM corresponds to TCP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.gethosename makes socket visible to outside world.
server_socket.bind((socket.gethostname(), 1337))
server_socket.settimeout(1) # Set timeout to 1 second so accept() will become (somewhat nonblocking)
# Socket is simply an endpoint that send/receives data.
# It sits in a corresponding port-IP pair

# Prepare to listen to a single socket at most
server_socket.listen(1)

try:
    while True:
        # create connection socket, address -> IP address of where data coming from
        try:
            (client_socket, address) = server_socket.accept() # Note that accept here is blocking 
            # Remember sockets receive stream of data ( how much chunks of data we receive at a time)
            msg = client_socket.recv(1024) # MAX of 1024 bytes for the buffer
            print(msg.decode("utf-8"))

        except socket.timeout:
            pass

        # TODO
        # 1. Receive an HTTP request
        # 2. Parse it to retrieve filename
        # 3. Get file from directory
        # 4. Send HTTP response to client with file content (404 if file not found)

except KeyboardInterrupt:
    server_socket.close()
