import pytest

from prophetly.server import ApplicationServer
from prophetly import utils


cmd_arg_none = {'--port': None, '--upload_path': None}
cmd_arg_with_valid_port = {'--port': '8888', '--upload_path': None}
cmd_arg_with_invalid_port = {'--port': 'invalid', '--upload_path': None}

@pytest.fixture
def server_without_upload_path_arg():
    '''Returns an ApplicationServer without upload_path flag'''
    return ApplicationServer(cmd_arg_none)

@pytest.fixture
def server_without_port_arg():
    '''Returns an ApplicationServer without port flag'''
    return ApplicationServer(cmd_arg_none)

@pytest.fixture
def server_with_valid_port_arg():
    '''Return an ApplicationServer with a valid port (8888) flag'''
    return ApplicationServer(cmd_arg_with_valid_port)


def test_server_upload_path(server_without_upload_path_arg):
    assert server_without_upload_path_arg.settings['upload_path'][-7:] == 'uploads'

def test_server_default_port(server_without_port_arg):
    assert server_without_port_arg.port == 9009

def test_server_custom_port(server_with_valid_port_arg):
    assert server_with_valid_port_arg.port == 8888

def test_server_invalid_port():
    with pytest.raises(utils.exceptions.PortInvalid):
        ApplicationServer(cmd_arg_with_invalid_port)
