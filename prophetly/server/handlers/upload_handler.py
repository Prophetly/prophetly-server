import json
from os import listdir

from main_handler import MainHandler


class UploadHandler(MainHandler):
    def post(self):
        try:
            file_info = self.request.files['file'][0]

            with open(UPLOAD_DIR + '/' + file_info.filename, 'w') as req_file:
                req_file.write(file_info.body)

            self.write('some post')
        except Exception as e:
            raise

    def get(self):
        file_list = listdir(UPLOAD_DIR)
        r = json.dumps({'files': file_list})
        r = json.loads(r)
        self.write(r)

    def options(self):
        self.set_status(204)
        self.finish()
