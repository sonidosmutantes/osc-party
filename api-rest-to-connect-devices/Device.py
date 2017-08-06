# -*- coding: UTF-8 -*-

class Device:
    destination_ip = ""
    msg_source_ip = ""
    path_pre = ""
    path_post = ""

    def send_osc(self, value):
        raise NotImplemented
        
    def set_source_ip(self, ip):
        self.msg_source_ip = ip
    
    def set_filter_path(self, path):
        self.filter_path = path

#class 