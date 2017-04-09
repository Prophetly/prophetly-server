"""
 __________________
| Prophetly Server |

Command Line Interface to Prophetly's Time Series Forecasting Tool.

Visit https://github.com/Prophetly/prophetly-server for feedback.


Usage:
  prophetly-server start [--port=<PORT>] [--upload_path=<PATH>]
  prophetly-server (-h | --help)
  prophetly-server --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt

from . import __version__ as VERSION
from . import server


def main():
    arguments = docopt(__doc__, version='Prophetly Server {0}'.format(VERSION))
    print(arguments)

    s = server.ApplicationServer(arguments)
    s.start()
