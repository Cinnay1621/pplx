import unittest
from pplx import PerplexityAPI

class TestPerplexityAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = "your_api_key_here"
        self.api = PerplexityAPI(self.api_key)

    def test_send_request(self):
        messages = [
            {"role": "system", "content": "Be precise and concise."},
            {"role": "user", "content": "How many stars are there in our galaxy?"}
        ]
        response = self.api.send_request("llama-3-sonar-small-32k-online", messages)
        self.assertIn("choices", response)

if __name__ == "__main__":
    unittest.main()