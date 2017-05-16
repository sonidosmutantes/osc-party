#!/usr/bin/python

import gviz_api
import liblo, sys

# create server, listening on port 1234
try:
    server = liblo.Server(12345)
except liblo.ServerError, err:
    print str(err)
    sys.exit()

global data
data = []
description={}

def marder_callback(path, args, types, src):
	print "got Marder message '%s' from '%s'" % (path, src.get_url())
	D = {"time": liblo.time()}
	description = {"time": ("number", "time")} 
		
	c = 0
	tupla = ('time',)
	for a, t in zip(args, types):
		c = c + 1
#       print "argument of type '%s': %s" % (t, a)
		D['p'+str(c)] = a
		description['p'+str(c)]=('number', 'Parametro ' + str(c))
		tupla = tupla + ('p' + str(c),)

	print D
	print description
	data.append(D)
	data_table = gviz_api.DataTable(description)
	# Loading it into gviz_api.DataTable
	data_table.LoadData(data)
	
	# Creating a JSon string
#	json = data_table.ToJSon()
	json = data_table.ToJSon(columns_order=tupla)
	with open('pyout.json', 'w') as f:
		f.write(json)


server.add_method(None, None, marder_callback)

# Creating the data

# loop and dispatch messages every 100ms
while True:	
	server.recv(100)


