import tornado.ioloop
from tornado.web import Application

#TODO:use notification center to notify about import exceptions

from handlers import *

# global Prophet instance
#prophet = Prophet()

UPLOAD_DIR = '/Users/pravj-mac/Projects/prophetly-modules/prophetly-react/uploads'

def make_app():
    print 'make_app..'
    return Application([
        (r"/", MainHandler),
        (r"/upload", UploadHandler),
        (r"/column/(.+)", ColumnHandler),
        (r"/data", DataHandler),
        (r"/filedata/(.+)", FileDataHandler),
    ])

"""
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
"""
