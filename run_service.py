#!/usr/bin/env python

from aprsclient import pull
from subprocess import call

if __name__ == '__main__':
    puller = pull.Pull('b/N0*')
    while True:
        line = puller.get_a_line()
        call(["parse_aprs_packet.pl", line])
