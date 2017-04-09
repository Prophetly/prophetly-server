import os
import tornado
import SocketServer

import handlers
from prophetly.utils import exceptions

#TODO: use notification center to notify about import exceptions

class ApplicationServer(object):
    def __init__(self, arguments):
        self.port = 9009
        self.server = None

        self.settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'upload_path': os.path.join(os.path.dirname(__file__), 'uploads'),
            'port': self.port,
        }

        self.initialize(arguments)

    def initialize(self, arguments):
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
            raise exceptions.PortInvalid('port \"{0}\" is invalid'.format(_port_arg))

        self.settings['port'] = self.port

    def _create_server(self):
        return tornado.web.Application([
            (r"/", handlers.MainHandler),
            (r"/upload", handlers.UploadHandler),
            (r"/column/(.+)", handlers.ColumnHandler),
            (r"/data", handlers.DataHandler),
            (r"/filedata/(.+)", handlers.FileDataHandler),
        ], **self.settings)

    def start(self):
        self.server = self._create_server()

        try:
            self.server.listen(self.port)
        except SocketServer.socket.error as e:
            if e.args[0] == 48:
                raise exceptions.PortUnavailable('port \"{0}\" is already in use'.format(self.port))

        tornado.ioloop.IOLoop.instance().start()

    def stop(self):
        tornado.ioloop.IOLoop.instance.stop()
