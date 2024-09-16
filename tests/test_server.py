import grpc
import unittest
from unittest.mock import MagicMock
import users_pb2
import users_pb2_grpc
from server.app import UsersServicer

class TestUsersService(unittest.TestCase):
    def setUp(self):
        self.servicer = UsersServicer()

    def test_get_users(self):
        request = users_pb2.GetUsersRequest()
        response = self.servicer.GetUsers(request, None)
        self.assertIsInstance(response, users_pb2.GetUsersResponse)
        self.assertTrue(len(response.users) > 0)