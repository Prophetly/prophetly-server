# -*- coding: utf-8 -*-
from prophetly import __version__

_package_signature = \
"""
  ___                  _          _    _
 | _ \ _ _  ___  _ __ | |_   ___ | |_ | | _  _
 |  _/| '_|/ _ \| '_ \| ' \ / -_)|  _|| || || |
 |_|  |_|  \___/| .__/|_||_|\___| \__||_| \_, |
                |_|                       |__/
 Prophetly Server v{0}
""".format(__version__)

def package_signature(port):
    print(_package_signature)
    print((" Visit http://localhost:{0} ...".format(port)))
