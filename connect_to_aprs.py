#!/usr/bin/env python

import aprspacket
import base64
import couchdb
import socket
import sys
import time
import os
import simplejson

TEST = False
try:
    if sys.argv[1]=='test':
        TEST = True
except:
    pass

BUFFER_SIZE = 4096
SERVER_NAME = 'db0anf.de'
#'noam.aprs2.net'
SERVER_PORT = 14580

args = {
    'call_sign': 'N0DEC',
    'callpass': '14999',
    'server_command': ' filter b/N0DEC*'
}
# user mycall[-ss] pass passcode[ vers softwarename softwarevers[ UDP udpport][ servercommand]]

db = couchdb.Server('http://delqn.xen.prgmr.com:5984/')['aprs']

if __name__=='__main__':
    a = socket.create_connection( (SERVER_NAME, SERVER_PORT ))

    print a.recv(BUFFER_SIZE)
    a.send("user %(call_sign)s pass %(callpass)s vers appears 0.01 UDP 7388 %(server_command)s\n" % args)
    a.send("#%(server_command)s\n" % args)

    while 1:
        r = a.recv(BUFFER_SIZE)
        if r[0]!="#":
            '''
            packet=aprspacket.AprsFrame()
            packet.parseAprs(r)
            d = packet.payload.__dict__
            del d['parent']
            '''
            d = os.popen('./parse_aprs_packet.pl %s' % base64.b64encode(r)).readline().replace('"', '\"')
            print d
            db[str(time.time())] = simplejson.loads(d)


    a.close()

