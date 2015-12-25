import socket

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('service.conf')

HOST = config.get('aprs', 'server')
PORT = config.get('aprs', 'port')

KWARGS = {
    'call': config.get('aprs', 'callsign'),
    'pass': config.get('aprs', 'callpass'),
    'server_command': 'b/N1*',  # 'filter b/N0DEC',
}
# user mycall[-ss] pass passcode[ vers softwarename softwarevers[ UDP udpport][ servercommand]]

class Pull(object):
    def __init__(self, fltr):
        self._aprs_connection_initialized = False
        self._sock = socket.create_connection((HOST, PORT))
        self._filter = fltr

    def _init_connection(self):
        if not self._aprs_connection_initialized:
            self._sock.send(
                'user {call} pass {pass} vers appears 0.01 {server_command}\n'.format(**KWARGS))
            self._sock.send('#{}\n'.format(self._filter))
            self._aprs_connection_initialized = True

    def _apply_filter(self, fltr):
        """Filter responses server-side. Example fltr='b/N0DEC'"""


    def get_a_line(self):
        self._init_connection()
        line = []
        while not line or line[-1] != '\n':
            line.append(self._sock.recv(1))
        return ''.join(line[:-1])

    def __del__(self):
        self._sock.close()
