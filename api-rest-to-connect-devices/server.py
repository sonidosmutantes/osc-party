#!/usr/bin/python2
# -*- coding: UTF-8 -*-

"""
Server REST API listening on 5010 port
"""

# liblo thread reference: https://github.com/dsacre/pyliblo/blob/master/examples/test_server_thread.py

from __future__ import print_function
import flask
from flask import jsonify
from flask import jsonify, request
from flask import abort

import logging
import os
import json
import itertools
import sys
import liblo
import time

from OSCServer import OSCServer

# TODO/WARNING: send to broadcast address, seems liblo python bindings doesn't support it (a socket flag must be set)
# OSC server unable to listen to multicast messages from Liblo - GitHub
# https://github.com/attwad/python-osc/issues/18

# OSC servers (like a) thread pool
osc_server_pool = dict()

# JSON config file
config = ""
try:
    config = json.load( open(sys.argv[1], 'r') ) 
except:
    try:
        config = json.load( open("config.json",'r') )
    except Exception, e:
        print(e)
        sys.exit(1)

try:
    HIDRORGANO_IP = config["hidrorgano"]["ip"]
    HIDRORGANO_PORT = int(config["hidrorgano"]["port"])
except Exception, e:
    print(e)
    # HIDRORGANO_IP = "127.0.0.1"
    # HIDRORGANO_PORT = 9000
from Hidrorgano import HidrorganoMotor
hidro_list = list()
for i in range(1,5+1):
    hidro_list.append( HidrorganoMotor(HIDRORGANO_IP, HIDRORGANO_PORT, i) )

def filter_hidrorgano(path, args, types, src):
    """
        Control motores hidrórgano 
    """
    # print("Hidrórgano filter():")
    # print("Message from", src.url)
    # print("typespec:", types)
    # for a, t in zip(args, types):
    #     print("received argument %s of type %s" % (a, t))

    src_ip = src.url.split('osc.udp://')[1][:-1].split(':')[0] #TODO: use a reg exp
    # print("ip: ", src_ip)
 
    success = False
    value = args[0]
    for hidro_motor in hidro_list:
        # print("Path: %s"%path)
        # print("Hidro motor %i filter path %s"%(hidro_motor.motor_number,hidro_motor.filter_path))
        if hidro_motor.filter_path==path:
            
            hidro_motor.max = 3
            hidro_motor.min = 0.01
            try:
                # hidro_motor.send_osc( value/float(hidro_motor.max) )
                print("value %f"%value)
                if value/float(hidro_motor.max)>0.2:
                    svalue = 0
                else:
                    svalue = 1
                hidro_motor.send_osc( svalue )
                # hidro_motor.send_osc( value ) #TODO: add mapping function (linear/exp, etc)
                success = True
            except liblo.AddressError as err:
                print(err)

        # # filtra por IP
        # if src_ip==hidro_motor.msg_source_ip:
        #     print("source_ip motor %i: "%hidro_motor.motor_number, hidro_motor.msg_source_ip)
#hidrorgano()

def filter_sillas(path, args, types, src):
    """
        Control motor sillas
    """
    print("Sillas filter():")
    print("message from", src.url)
    print("message from", src.ip)
    print("typespec:", types)
    for a, t in zip(args, types):
        print("received argument %s of type %s" % (a, t))
    if src.url==sillas_msg_source_ip:
        pass
        #TODO: add sillas control

def filter_visuales(path, args, types, src):
    """
        Control motor sillas
    """
    print("Sillas filter():")
    print("message from", src.url)
    print("message from", src.ip)
    print("typespec:", types)
    for a, t in zip(args, types):
        print("received argument %s of type %s" % (a, t))
    if src.url==sillas_msg_source_ip:
        pass
        #TODO: add sillas control
#sillas()

def fallback(path, args, types, src):
    print("got unknown message '%s' from '%s'" % (path, src.url))
    for a, t in zip(args, types):
        print("argument of type '%s': %s" % (t, a))
#()

#tmp test method
# def test_input(path, args, types, src):
#     print("bar_cb():")
#     print("message from", src.url)
#     print("typespec:", types)
#     for a, t in zip(args, types):
#         print("received argument %s of type %s" % (a, t))


#################
### FLASK app ###
#################

app = flask.Flask(__name__)
# auto = Autodoc(app) # automatic doc

@app.route('/reset', methods=['POST'])
def post_reset_device():
    """
        Create an OSC server on PORT number
        Use: liblo.ServerThread() to random free port
    """
    try:
        device = request.headers['Device']
        return device
    except liblo.ServerError as err:
        print(err)
        abort(404)

@app.route('/create', methods=['POST'])
def post_create_osc_server():
    """
        Create an OSC server on PORT number
        Use: liblo.ServerThread() to random free port
    """
    try:
        port = request.headers['Port']

        # create server, listening on port PORTNUMBER
        if port=="*":
            osc_server = OSCServer("") # free port is chosen
        else:
            osc_server = OSCServer(port)

        print("Created OSCServer thread on port", osc_server.port)

        osc_server_pool[port] = osc_server

        osc_server.start()

        return str(osc_server.port)
    except liblo.ServerError as err:
        print(err)
        abort(404)
#()

@app.route('/filter', methods=['POST'])
def post_filter():
    """
        From host: ip:port
        To host: ip:port
        Destination address: 
    """
    try:
        #parse header
        port = request.headers['Port']
        from_host = request.headers['From']
        to_host = request.headers['To']
        addr = request.headers['Addr']
        msg_type = request.headers['Type']
        device = request.headers['Device']
        
        #specific device
        motor = ""
        try:
            motor = request.headers['Motor']
        except:
            pass #TODO: add logging

        auth_header = request.headers['Authorization']
        # if auth_header: #TODO: check auth
        
        osc_server = osc_server_pool[port]


        # osc_server.add_method(addr, msg_type, test_input)
        if addr=="*":
            # addr = None #FIXME: no works
            osc_server.add_method(None, msg_type, filter_hidrorgano)
            if msg_type=="*":
               osc_server.add_method(None, None, filter_hidrorgano)
        else:
            osc_server.add_method(addr, msg_type, filter_hidrorgano)

        # register a fallback for unhandled messages
        if device=="hidrorgano":
            osc_server.filters.append(filter_hidrorgano)
        elif device=="sillas":
            osc_server.filters.append(filter_sillas)
        elif device=="visuales":
            osc_server.filters.append(filter_visuals)

        for hidro in hidro_list:
            if motor==str(hidro.motor_number):
                hidro.set_source_ip( from_host )
                hidro.set_filter_path( addr )
                print("hidro motor %i sat with filter path: %s"%(hidro.motor_number, addr))

        print("Connect address %s of type %s"%(addr,msg_type))
        return "Ok"
    except Exception, e:
        print(e)
        abort(404)
#()

if __name__ == "__main__":
    file_handler = logging.FileHandler('api_ws.log')
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.run( debug=True, host="0.0.0.0", port=5010 )