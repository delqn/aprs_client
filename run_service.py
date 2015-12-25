#!/usr/bin/env python

from aprsclient import pull

if __name__ == '__main__':
    puller = pull.Pull('b/N0*')
    while True:
        print puller.get_a_line()
