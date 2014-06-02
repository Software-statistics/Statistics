# -*- coding: utf-8 -*-
import BaseHTTPServer
import CGIHTTPServer

HOST = ''
PORT = 8007

if __name__=='__main__':
	server = BaseHTTPServer.HTTPServer((HOST, PORT),CGIHTTPServer.CGIHTTPRequestHandler)
	print("start")
	server.serve_forever()

