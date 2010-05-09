#!/usr/bin/env python2.6
# coding=utf-8
"""
* Copyright © 2010 by Thomas Roth <code@leveldown.de>
*
* This code is licensed under GPLv3. You should've received a copy of the
* license with this package.
"""

import sys
import SimpleXMLRPCServer
import nmap

class Scanner:
	scanner = None
	def __init__(self):
		self.scanner = nmap.PortScanner()

	#Scan a host:
	def scan(self, ip, ports):
		self.scanner.scan(ip,ports)

#Working with scan results:
	# Get nmap cmd
	def command_line(self):
		return self.scanner.command_line()
	# Get scan informations
	def scaninfo(self):
		return self.scanner.scaninfo()
	# Get all hosts
	def all_hosts(self):
		return self.scanner.all_hosts()

#Working with hosts in result:

	# Get hostname
	def hostname(self, host):
		return self.scanner[host].hostname()
	# Get state
	def state(self, host):
		return self.scanner[host].state()
	# Get all protocols
	def all_protocols(self, host):
		return self.scanner[host].all_protocols()

	# Has protocol?
	def has_protocol(self, host, key):
		return self.scanner[host].has_key(key)

	def ports(self, host, protocol):
		return self.scanner[host][protocol].keys()

	def port(self, host, protocol, port):
		try:
			return self.scanner[host][protocol][port]
		except KeyError:
			return None

nm = Scanner()

if len(sys.argv) != 3:
	print 'Usage: %s [bind] [port]' % sys.argv[0]
	exit()

port = 0
try: 
	port = int(sys.argv[2])
except ValueError:
	print 'Port has to be an integer.'
	exit()

server = SimpleXMLRPCServer.SimpleXMLRPCServer(
	(sys.argv[1], port),
	allow_none=True)

server.register_instance(nm)

try:
	print 'Listening on %s:%s' % (sys.argv[1], sys.argv[2])
	server.serve_forever()
except KeyboardInterrupt:
	print 'Exiting.'
