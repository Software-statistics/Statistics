# A messy HTTP server based on TCP socket 

import socket
import html
import singleprice

# Address
HOST = ''
PORT = 8000

# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# Serve forever
while True:
    s.listen(3)
    conn, addr = s.accept()                    
    request    = conn.recv(1024)         # 1024 is the receiving buffer size
    method     = request.split(' ')[0]
    src        = request.split(' ')[1]

    print 'Connected by', addr
    print 'Request is:', request

    # if GET method request
    if method == 'GET':
        content = html.indexpage()
        # send message
        conn.sendall(content)
    # if POST method request
    if method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')             # Find the empty line
        entry = form[idx:]               # Main content of the request

        try:
            first = entry[-1].split('=')[1].split('&')[0]
            second = entry[-1].split('=')[2].split('&')[0]
            third = entry[-1].split('=')[3]
            print first
            print second
            print third
        except:
            pass
        html.addtable(singleprice.highchart('B003YUC4YI'))
        html.addtable(singleprice.highchart('B003YUC4YI'))
        content = html.head() + html.body0('B003YUC4YI') + html.foot()

        value = entry[-1].split('=')[-1]
        
        #content = html.head() + html.body(singleprice.highchart('B003YUC4YI')) + html.foot()
        conn.sendall(content)
        ######
        # More operations, such as put the form into database
        # ...
        ######
    # close connection
    conn.close()
