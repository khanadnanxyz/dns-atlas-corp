import json

try:
    from app import app
    import unittest
except Exception as e:
    print('Modules Missing {}'.format(e))


class AtlasTest(unittest.TestCase):

    def test_index_route(self):
        client = app.test_client()
        url = '/'

        response = client.get(url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_index_content(self):
        client = app.test_client()
        url = '/'

        response = client.get(url)
        content_type = response.content_type
        self.assertEqual(content_type, 'application/json')

    def test_index_data(self):
        client = app.test_client()
        url = '/'

        response = client.get(url)
        data = response.data
        print(data)
        self.assertTrue(b'{"message":"hello, space!","status":"OK"}\n' in data)

    def test_loc_route_success(self):
        client = app.test_client()
        url = '/api/v1/loc'

        mock_request_data = {
            "x": "123.12",
            "y": "456.56",
            "z": "789.89",
            "vel": "50.0"
        }

        response = client.post(url, data=json.dumps(mock_request_data))
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_loc_empty_data_failure(self):
        client = app.test_client()
        url = '/api/v1/loc'

        mock_request_data = {}

        response = client.post(url, data=json.dumps(mock_request_data))
        status_code = response.status_code
        self.assertEqual(status_code, 400)

    def test_loc_faulty_data_failure(self):
        client = app.test_client()
        url = '/api/v1/loc'

        mock_request_data = {
            "x": "123.12",
            "y": "456.56",
            "z": "south",
            "vel": ""
        }

        response = client.post(url, data=json.dumps(mock_request_data))
        status_code = response.status_code
        self.assertEqual(status_code, 422)

    def test_loc_response_success(self):
        client = app.test_client()
        url = '/api/v1/loc'

        mock_request_data = {
            "x": "123.12",
            "y": "456.56",
            "z": "789.89",
            "vel": "20.0"
        }

        response = client.post(url, data=json.dumps(mock_request_data))
        data = response.data
        print(data)
        self.assertTrue(b'{"loc":1389.57}\n' in data)


if __name__ == "__main__":
    unittest.main()
