import os
import tornado.ioloop
from tornado.web import Application

from handlers import *

#TODO: use notification center to notify about import exceptions

def create_server(arguments):
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "upload_path": os.path.join(os.path.dirname(__file__), "uploads"),
    }

    # custom 'upload_path' supplied as command line flags
    if arguments['--upload_path'] is not None:
        settings['upload_path'] = arguments['--upload_path']

    return Application([
        (r"/", MainHandler),
        (r"/upload", UploadHandler),
        (r"/column/(.+)", ColumnHandler),
        (r"/data", DataHandler),
        (r"/filedata/(.+)", FileDataHandler),
    ], **settings)
