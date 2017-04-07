"""
 __________________
| Prophetly Server |

Command Line Interface to Prophetly's Time Series Forecasting Tool.

Visit https://github.com/Prophetly/prophetly-server for feedback.


Usage:
  prophetly-server start [--host=<HOST>] [--port=<PORT>]
  prophetly-server (-h | --help)
  prophetly-server --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
from tornado import ioloop

from server import make_app

def main():
    arguments = docopt(__doc__, version='Prophetly Server 0.1.18')
    print(arguments)

    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
