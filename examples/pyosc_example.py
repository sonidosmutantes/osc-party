#!/usr/bin/env python3

"""
sudo pip install git+git://github.com/ptone/pyosc.git
"""

from OSC import OSCClient, OSCMessage

addr = "127.0.0.1" #localhost
port = 4330

client = OSCClient()
client.connect( (addr, port )

client.send( OSCMessage("/user/value", [0.5] ) )


