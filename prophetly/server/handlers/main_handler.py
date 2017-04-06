from tornado.web import RequestHandler
from pkg_resources import resource_filename


class MainHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3000")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Cache-Control")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Access-Control-Allow-Credentials", "true")

    def get(self):
        index_template = resource_filename('prophetly.server.static', 'template.html')
        self.render(index_template, prophetly_server_address='http://localhost:8888')
