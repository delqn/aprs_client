import socket

BUFFER_SIZE = 4096
SERVER_NAME = 'second.aprs.net'
SERVER_PORT = 10152

args = {
    'call_sign': 'N0DEC',
    'callpass': '14999',
    'server_command': 'filter b/N0DEC'
}
# user mycall[-ss] pass passcode[ vers softwarename softwarevers[ UDP udpport][ servercommand]]

a = socket.create_connection( (SERVER_NAME, SERVER_PORT ))

print a.recv(BUFFER_SIZE)

a.send("user %(call_sign)s pass %(callpass)s vers appears 0.01 %(server_command)s\n" % args)
#a.send("#%(filter)s\n" % args)

rows = 0
while rows <= 10:
    print a.recv(BUFFER_SIZE)
    rows += 1

a.close()
