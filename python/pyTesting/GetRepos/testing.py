import unittest
from unittest.mock import patch, MagicMock
from functions import send_req, print_data

class test_send_req(unittest.TestCase):

    def test_send_req_no_parameter_passed(self):
        self.assertRaises(TypeError, send_req) # calling send_req without any parameters

    def test_send_req_parameter_type(self):
        self.assertRaises(TypeError, send_req, 1) # calling send_req with non string

    @patch('functions.requests.get')
    def test_send_req_called_with(self, mock_get_requests): 
        send_req("mostafa-abokhadra")
        mock_get_requests.assert_called_with(
            f"https://api.github.com/users/mostafa-abokhadra/repos")
    
    @patch('functions.requests.get')
    def test_send_req_expected_results(self, mock_get_requests):
        result = {"name": "mostafa-abokhadra"}
        mock_res = MagicMock()
        mock_res.json.return_value = result
        mock_get_requests.return_value = mock_res
        self.assertEqual(send_req("mostafa-abokhadra"), result)
    
    @patch('functions.requests.get')
    def test_send_req_return_type(self, mock_get_requests):
        result = {"name": "mostafa"}
        response = MagicMock()
        response.json.return_value = result
        mock_get_requests.return_value = result
        self.assertIsInstance(mock_get_requests.return_value, dict)

class test_print_data(unittest.TestCase):
    def test_print_data_no_parameters(self):
        self.assertRaises(TypeError, print_data)
    def test_print_data_parameter_type(self):
        self.assertRaises(TypeError, print_data, {"name": "mostafa-abokhadra"})
    def test_print_data_expected_results(self):
        self.assertEqual(print_data([{"name": "mostafa Abokhadra"}]), True)

if __name__ == '__main__':
    unittest.main()