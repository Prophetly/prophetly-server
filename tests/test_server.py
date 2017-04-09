import re
import json
import pytest

from prophetly import server
from prophetly import utils


"""
pytest fixture data
"""

cmd_arg_none = {'--port': None, '--upload_path': None}
cmd_arg_with_valid_port = {'--port': '8888', '--upload_path': None}
cmd_arg_with_invalid_port = {'--port': 'invalid', '--upload_path': None}

"""
pytest fixtures
"""

@pytest.fixture
def server_without_upload_path_arg():
    '''Returns an ApplicationServer without upload_path flag'''
    return server.ApplicationServer(cmd_arg_none)

@pytest.fixture
def server_without_port_arg():
    '''Returns an ApplicationServer without port flag'''
    return server.ApplicationServer(cmd_arg_none)

@pytest.fixture
def server_with_valid_port_arg():
    '''Return an ApplicationServer with a valid port (8888) flag'''
    return server.ApplicationServer(cmd_arg_with_valid_port)

@pytest.fixture
def app():
    application = server.ApplicationServer(cmd_arg_with_valid_port)
    return application._create_server()

"""
pytest testable functions
"""

def test_server_upload_path(server_without_upload_path_arg):
    assert server_without_upload_path_arg.settings['upload_path'][-7:] == 'uploads'

def test_server_default_port(server_without_port_arg):
    assert server_without_port_arg.port == 9009

def test_server_custom_port(server_with_valid_port_arg):
    assert server_with_valid_port_arg.port == 8888

def test_server_invalid_port():
    with pytest.raises(utils.exceptions.PortInvalid):
        server.ApplicationServer(cmd_arg_with_invalid_port)

@pytest.mark.gen_test
def test_server_side_rendering(http_client, base_url):
    response = yield http_client.fetch(base_url)

    response_match = re.search(r'http://localhost:([0-9]+)', response.body)
    assert response_match.group(1) == cmd_arg_with_valid_port['--port']

@pytest.mark.gen_test
def test_empty_upload_path(http_client, base_url):
    response = yield http_client.fetch('{0}/upload'.format(base_url))
    response_dict = json.loads(response.body)
    assert len(response_dict['files']) == 0
