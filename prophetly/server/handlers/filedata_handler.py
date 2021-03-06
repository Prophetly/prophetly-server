import os
import pandas as pd

from .main_handler import MainHandler
from prophetly.utils import exceptions


class FileDataHandler(MainHandler):
    def get(self, file_param):
        df = pd.read_csv(os.path.join(self.settings['upload_path'], file_param))

        cols = df.columns.tolist()
        res = {'columns': cols, 'rows': []}

        for index, row in df.iterrows():
            row_dict = {}
            for col in cols:
                row_dict[col] = row[col]
            res['rows'].append(row_dict)

        self.write(res)

    def post(self, file_param):
        try:
            os.remove(os.path.join(self.settings['upload_path'], file_param))
        except OSError:
            raise exceptions.FileDeleteError('Unable to delete file {0}'.format(file_param))

        self.write({'status': 'OK'})
