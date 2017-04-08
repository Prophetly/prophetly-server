import os
import json
import pandas as pd

from main_handler import MainHandler


class ColumnHandler(MainHandler):
    def get(self, file_param):
        df = pd.read_csv(os.path.join(self.settings['upload_path'], file_param))
        res = {'columns': [{'value': col.encode('utf-8'), 'label': col.encode('utf-8')} for col in df.columns.tolist()]}

        ans = json.loads(json.dumps(res))
        self.write(ans)
