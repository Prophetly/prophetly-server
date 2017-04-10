# -*- coding: utf-8 -*-

import os
import sys


def version():
    ''' Return the major (2/3) version of system python '''
    return sys.version_info[0]

def exec_env():
    ''' Return the execution environment for package '''
    return os.environ.get('EXEC_ENV')

def is_env_build():
    ''' Check if the current environment is TRAVIS continuous integration '''
    return exec_env() == 'TRAVIS'
