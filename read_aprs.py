import serial
import sys

def command(s, command, *args):
    cmd = command
    if args:
        cmd += " " + " ".join(args)
    print "PC->D72: %s" % cmd
    s.write(cmd + "\r")

    result = ""
    while not result.endswith("\r"):
        result += s.read(8)

    print "D72->PC: %s" % result.strip()

    return result.strip()


def l2b(*l):
    r = ''
    for v in l:
        if type(v) is str:
            r += v
        else:
            r += chr(v)
    return r

def bin2hex(v):
    r = ''
    for i in range(len(v)):
        r += '%02x '%ord(v[i])
    return r

def bin_cmd(s, rlen, *b):
    if b is not None:
        cmd = l2b(*b)
    else:
        cmd = ''
    print "PC->D72: %s" % cmd
    s.write(cmd)
    result = bin2hex(s.read(rlen)).strip()
    print "D72->PC: %s" % result
    return result

def usage(argv):
    print "Usage: %s <serial device> <read-image>" % argv[0]
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        usage(sys.argv)

    s = serial.Serial(port=sys.argv[1], baudrate=9600, xonxoff=True, timeout=0.25)

    #print get_id(s)
    #print get_memory(s, int(sys.argv[2]))
    print command(s, 'TC 1')
    print command(s, 'ID')
    print command(s, 'TY')
    print command(s, 'FV 0')
    print command(s, 'FV 1')
    print bin_cmd(s, 4, '0M PROGRAM\r')
    s.setBaudrate(57600)
    s.getCTS()
    s.setRTS()
    of = file(sys.argv[2], 'wb')
    for i in range(256):
        sys.stdout.write('\rfetching block %d...' % i)
        sys.stdout.flush()
        s.write(l2b(0x52, 0, i, 0, 0))
        s.read(5) # command response first
        of.write(s.read(256))
        s.write('\x06')
        s.read()
    print
    of.close()
    print bin2hex(s.read(5))
    print bin2hex(s.read(1))
    print bin_cmd(s, 2, 'E')
    s.getCTS()
    s.setRTS()
    s.getCTS()
    s.getCTS()
    s.close()
