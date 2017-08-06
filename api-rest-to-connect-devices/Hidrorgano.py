# -*- coding: UTF-8 -*-
import liblo
from Device import Device

class HidrorganoMotor(Device):
    """
       Hidrórgano paths
       
       /hidrorgano/motor/[NRO_MOTOR]/remote
       Con NRO_MOTOR en el rango 0..4
       Que se manda un int, en 1 para encendido y 0 para apagado.
       (si no es int, no reconoce el tipo y falla)
       
       Escucha en el 9000 y el broadcast lo hace en el 9001
    """
    path_pre = "/hidrorgano/motor/"
    path_post = "/remote"

    def __init__(self, dest_ip, osc_port=9000, motor_number=1):
        self.destination_ip = dest_ip
        self.osc_port = osc_port
        self.motor_number = motor_number
        self.filter_path = ""

    def send_osc(self, value):
        # value = float(value) #no forzar conversión, recibe int
        target = liblo.Address(self.destination_ip, self.osc_port)
        path = self.path_pre + str(self.motor_number) + self.path_post
        liblo.send(target, path, value)
        print( "HIDRO:: sending %s to %s:%s with value %f"%(path, self.destination_ip, str(self.osc_port), value) )
#class
