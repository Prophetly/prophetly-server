import os
import json

from .main_handler import MainHandler


class UploadHandler(MainHandler):
    def post(self):
        try:
            print(self.request)
            print(self.request.files)
            file_info = self.request.files['file'][0]

            with open(os.path.join(self.settings['upload_path'], file_info.filename), 'w') as req_file:
                req_file.write(file_info.body)

            self.write('some post')
        except Exception as e:
            raise

    def get(self):
        if not os.path.isdir(self.settings['upload_path']):
            os.makedirs(self.settings['upload_path'])

        file_list = os.listdir(self.settings['upload_path'])

        r = json.dumps({'files': file_list})
        r = json.loads(r)
        self.write(r)

    def options(self):
        self.set_status(204)
        self.finish()
