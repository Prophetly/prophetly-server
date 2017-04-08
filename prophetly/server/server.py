import os
import tornado
import SocketServer

from handlers import *
from prophetly.utils import PortInvalid, PortUnavailable

#TODO: use notification center to notify about import exceptions

class ApplicationServer(object):
    def __init__(self, arguments):
        self.port = 9009
        self.server = None

        self.settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'upload_path': os.path.join(os.path.dirname(__file__), 'uploads'),
        }

        # custom 'upload_path' supplied as command line flag
        _path_arg = arguments['--upload_path']

        # custom 'port' supplied as command line flag
        _port_arg = arguments['--port']

        if _path_arg is not None:
            self.settings['upload_path'] = _path_arg

        if _port_arg is None:
            pass
        elif _port_arg is not None and _port_arg.isdigit():
                self.port = int(_port_arg)
        else:
            raise PortInvalid('port {0} is invalid'.format(_port_arg))

    def create_server(self):
        return tornado.web.Application([
            (r"/", MainHandler),
            (r"/upload", UploadHandler),
            (r"/column/(.+)", ColumnHandler),
            (r"/data", DataHandler),
            (r"/filedata/(.+)", FileDataHandler),
        ], **self.settings)

    def start(self):
        self.server = self.create_server()

        try:
            self.server.listen(self.port)
        except SocketServer.socket.error as e:
            if e.args[0] == 48:
                raise PortUnavailable("port {0} is already in use".format(self.port))

        tornado.ioloop.IOLoop.instance().start()

    def stop(self):
        tornado.ioloop.IOLoop.instance.stop()
