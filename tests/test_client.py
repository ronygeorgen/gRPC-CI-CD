import unittest
from unittest.mock import patch, MagicMock
import grpc
import users_pb2
import users_pb2_grpc
from client.app import run

class TestClientApp(unittest.TestCase):
    @patch('grpc.insecure_channel')
    def test_run(self, mock_channel):
        mock_stub = MagicMock()
        mock_channel.return_value.__enter__.return_value = mock_stub
        
        mock_response = users_pb2.GetUsersResponse()
        mock_user = mock_response.users.add()
        mock_user.id = "1"
        mock_user.name = "Test User"
        
        mock_stub.GetUsers.return_value = mock_response
        
        run()
        
        mock_stub.GetUsers.assert_called_once_with(users_pb2.GetUsersRequest())