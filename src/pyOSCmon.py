#!/usr/bin/python

from liblo import *
import liblo
import gviz_api
import sys
import simplejson
from time import sleep

#WWW_PATH="/var/www/"
#WWW_PATH="/var/www/html/"
WWW_PATH="./"

PORT=4330

#clean file at startup
f = open(WWW_PATH+"labellist.json", "w")
f.close()

class MyServer(ServerThread):
    def __init__(self):
        ServerThread.__init__(self, PORT) #FIXME: load port from json config file

    gdata_dict = {}
    ets_dict ={}
    val_dict = {}
    t0 = liblo.time()

    @make_method(None, None)
    def fallback(self, path, args, src):
	lista = path.split("/")
	n_lista = len(lista)

#	print self.ets_dict

	etiqueta = '/'+'/'.join(lista[1:n_lista])
	file_etiqueta = '_'.join(lista[1:n_lista])

	if self.ets_dict.get(etiqueta,'Nueva')=='Nueva':
		self.gdata_dict[etiqueta]=[]
		self.ets_dict[etiqueta]=[len(args), file_etiqueta]
		f = open(WWW_PATH+"labellist.json", "w")
                #print(WWW_PATH)
		f.write(simplejson.dumps(self.ets_dict)) # Write a string to a file
		f.close()
		print src , path

	if not(args):

		for c,dt in zip([0, 1, 0],[0,1,2]):

			tupla = ('time',)

			self.val_dict[etiqueta]={}
			self.val_dict[etiqueta]['data'] = {"time": round(liblo.time()-self.t0,2)+dt/1000}
			self.val_dict[etiqueta]['description'] = {"time": ("number", "time")}

			self.val_dict[etiqueta]['data']['e'] = c
			self.val_dict[etiqueta]['description']['e']=('number', 'Evento')
			tupla = tupla + ('e',)

			self.gdata_dict[etiqueta].append(self.val_dict[etiqueta]['data'])

	else:
		self.val_dict[etiqueta]={}
		self.val_dict[etiqueta]['data'] = {"time": round(liblo.time()-self.t0,2)}
		self.val_dict[etiqueta]['description'] = {"time": ("number", "time")}

		c = 0
		tupla = ('time',)

		for a in args:
			c = c + 1
			self.val_dict[etiqueta]['data']['p'+str(c)] = a
			self.val_dict[etiqueta]['description']['p'+str(c)]=('number', 'Parametro ' + str(c))
			tupla = tupla + ('p' + str(c),)

# log
#		print self.val_dict[etiqueta]['data']
#		print self.val_dict[etiqueta]['description']
#		print self.gdata_dict[etiqueta]
#		import ipdb;ipdb.set_trace()

		self.gdata_dict[etiqueta].append(self.val_dict[etiqueta]['data'])

	if len(self.gdata_dict[etiqueta]) > 100:
		self.gdata_dict[etiqueta].pop(0)

	data_table = gviz_api.DataTable(self.val_dict[etiqueta]['description'])

	# Loading it into gviz_api.DataTable
	data_table.LoadData(self.gdata_dict[etiqueta])

	# Creating a JSon string
	json = data_table.ToJSon(columns_order=tupla)

	with open(WWW_PATH+file_etiqueta +'.json', 'w') as f:
		f.write(json)
	f.close()


try:
    server = MyServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()
#raw_input("press enter to quit...\n")
#print("Listening at %s"%PORT)
 
while True:
    #server.recv(100) #every 100ms (it's a thread)
    sleep(.1)
