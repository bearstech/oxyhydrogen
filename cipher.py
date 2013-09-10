#!/usr/bin/env python
import socket, sys
#!/usr/bin/env python

from OpenSSL import SSL


def verify_cb(conn, cert, errnum, depth, ok):
    # This obviously has to be updated
    #print 'Got certificate: %s' % cert.get_subject()
    return ok


for method_name, method in [("SSLv23", SSL.SSLv23_METHOD), ("TLSv1", SSL.TLSv1_METHOD)]:
    print "#", method_name
    ctx = SSL.Context(method)
    ctx.set_verify(SSL.VERIFY_PEER, verify_cb) # Demand a certificate


    sock = SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    sock.connect((sys.argv[1], int(sys.argv[2])))

    sock.do_handshake()
    ciphers = sock.get_cipher_list()
    sock.close()

    for cipher in ciphers:
        ctx.set_cipher_list(cipher)
        sock = SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        sock.connect((sys.argv[1], int(sys.argv[2])))
        try:
            sock.do_handshake()
            print " ", cipher
            sock.close()
        except SSL.Error:
            print "!", cipher

    #print sock.get_peer_cert_chain()
    #print sock.get_cipher_list()
    #print dir(sock.get_context())
