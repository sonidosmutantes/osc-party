import liblo
from liblo import make_method

class OSCServer(liblo.ServerThread):
    """
        OSC server
    """
    def __init__(self, port):
        liblo.ServerThread.__init__(self, port)
        self.debug = True #Received osc msg to std output

        self.filters = list()
    #()

    # @make_method("/user/value", 'f')
    # def update_callback(self, path, args):
    # #()

    # @make_method(None, 'f')
    # def float_fallback(self, path, args):
    #     print("received message '%s'" % path)
    # #()

    @make_method(None, None)
    def update_state_fallback(self, path, args, types, src):
        msg = path[1:]
        value = args[0]
        # print("[%s] Received %s %s"%(str(self.port),path,args))
        for f in self.filters:
            f(path,args,types,src)
    #()

#class