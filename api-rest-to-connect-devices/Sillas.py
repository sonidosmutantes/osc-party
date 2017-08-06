# -*- coding: UTF-8 -*-
import liblo
from Device import Device

class SillasMotor(Device):
    """
        Sillas. Cada una una ip distinta!
        path ->  "/1/toggleLED/" (1. activa, 0. detiene)
        puerto 8000
        ip 5.0.0.100 y 5.0.0.101
    """
    path_pre = "/1/toggleLED/"
    path_post = ""

    def __init__(self, dest_ip, osc_port=8000, motor_number=1):
        self.destination_ip = dest_ip
        self.osc_port = osc_port
        self.motor_number = motor_number
        self.filter_path = ""

    def send_on(self):
        self.send_osc(1.)

    def send_off(self):
        self.send_osc(0.)

    def send_osc(self, value):
        target = liblo.Address(self.destination_ip, self.osc_port)
        path = "/1/toggleLED/"
        value = 0.
        liblo.send(target, path, value)
        print( "SILLAS:: sending %s to %s:%s with value %f"%(path, self.destination_ip, str(self.osc_port), value) )