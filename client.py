#!/usr/bin/env python2.6
# coding=utf-8
""" 
* Copyright © 2010 by Thomas Roth <code@leveldown.de>
*
* Permission to use, copy, modify, and/or distribute this software for any
* purpose with or without fee is hereby granted, provided that the above
* copyright notice and this permission notice appear in all copies.
*
* THIS SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
* WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
* MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
* ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
* WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
* ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
* OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")

server.scan('127.0.0.1', '22-443')

print server.command_line()
print server.scaninfo()

hosts = server.all_hosts()
for host in hosts:
	print ' '+server.hostname(host)
	print ' '+server.state(host)

	protocols = server.all_protocols(host)
	for protocol in protocols:
		print '  ' + str(protocol)
		ports = server.ports(host, protocol)
		for port in ports:
			print '   ' + str(port)
