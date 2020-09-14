import socket

#----------------------------------------Socket Definitions----------------------------------------
BUFFER_SIZE = 1024              # MAX of 1024 bytes for the buffer of http header
ENCODE_FORMAT = "utf-8"         # Message encoder format


def write_http_header(socket, message):
    encoded_message = bytes(message, ENCODE_FORMAT)
    socket.send(encoded_message)

def write_http_body(socket, message):
    # Mostly taken from https://docs.python.org/3.8/howto/sockets.html#using-a-socket
    totalsent = 0
    while totalsent < len(message):
        sent = socket.send(message[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

def read_http_header(socket):
    received_message = socket.recv(BUFFER_SIZE).decode(ENCODE_FORMAT)
    return received_message

def read_http_body(socket, content_length):
    # Mostly taken from https://docs.python.org/3.8/howto/sockets.html#using-a-socket
    chunks = []
    bytes_recd = 0
    while bytes_recd < content_length:
        chunk = socket.recv(min(content_length - bytes_recd, BUFFER_SIZE))
        if chunk == b'':
            raise RuntimeError("socket connection broken") 
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    file_content = b''.join(chunks)

    return file_content


if __name__ == "__main__":
    # unit tests for tcpSocket file
    
    # Newsocket = Socket()
    # Newsocket.connect()
    pass
    