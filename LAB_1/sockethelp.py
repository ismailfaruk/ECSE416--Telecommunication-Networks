import socket

#----------------------------------------Socket Definitions----------------------------------------
# Server Definitions
Host = socket.gethostname()     # Sets the current computer name as hostname
Port = 1337                     # low number ports are usually reserved, use a nice high number (4 digits) https://docs.python.org/3.5/howto/sockets.html
BufferSize = 1024               # MAX of 1024 bytes for the buffer
EncodeFormat = "utf-8"          # Message encoder format
Timeout = 5                     # Set timeout to 1 second so accept() will become (somewhat nonblocking)

# _Host = socket.gethostname()     # Sets the current computer name as hostname
# _Port = 1337                     # low number ports are usually reserved, use a nice high number (4 digits) https://docs.python.org/3.5/howto/sockets.html
# _Timeout = 1                     # Set timeout to 1 second so accept() will become (somewhat nonblocking)
# _MaxRequest = 1                  # Prepared to listen to a single socket at most
# _BufferSize = 1024               # MAX of 1024 bytes for the buffer
# _EncoderFormat = "utf-8"         # Message encoder format
#--------------------------------------------------------------------------------------------------

# class Socket:
#     def __init__(self, Host = _Host, Port = _Port, Timeout = _Timeout, EncoderFormat = _EncoderFormat):
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.Host = Host
#         self.Port = Port
#         self.Timeout = Timeout
#         self.EncoderFormat = EncoderFormat

#     def connect(self):
#         self.socket.connect((self.Host, self.Port))
#         return socket

#     def Read(self, Socket):
#         RecievedMessage = self.socket.recv(_BufferSize).decode(_EncoderFormat)
#         return RecievedMessage
        
#     def Write(self, Socket, Message):
#         EncodedMessage = bytes(Message, self.EncoderFormat)
#         self.socket.send(EncodedMessage)

def write(Socket, Message):
    EncodeFormat = "utf-8"
    EncodedMessage = bytes(Message, EncodeFormat)
    Socket.send(EncodedMessage)

def read(Socket):
    # TODO: implement a good reader
    RecievedMessage = Socket.recv(BufferSize).decode(EncodeFormat)
    return RecievedMessage

if __name__ == "__main__":
    # unit tests for tcpSocket file
    
    # Newsocket = Socket()
    # Newsocket.connect()
    pass
    