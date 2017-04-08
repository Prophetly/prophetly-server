import os
import tornado

from handlers import *

#TODO: use notification center to notify about import exceptions

class ApplicationServer(object):
    def __init__(self, arguments):
        self.server = None

        self.settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'upload_path': os.path.join(os.path.dirname(__file__), 'uploads'),
        }

        # custom 'upload_path' supplied as command line flags
        if arguments['--upload_path'] is not None:
            self.settings['upload_path'] = arguments['--upload_path']

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
        self.server.listen(8888)
        
        tornado.ioloop.IOLoop.current().start()
