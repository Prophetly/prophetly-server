import pytest

from server import ApplicationServer


@pytest.fixture
def server_without_upload_path_arg():
    '''Returns an ApplicationServer without upload_path flag'''
    return ApplicationServer({'--upload_path': None})

def test_server_upload_path(server_without_upload_path_arg):
    assert server_without_upload_path_arg.settings['upload_path'][-7:] == 'uploads'
