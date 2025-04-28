import requests
import unittest


class TestNewJoke(unittest.TestCase):
    def setUp(self):
        self.url = "https://api.chucknorris.io/jokes/random"

    def test_create_new_random_joke(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200, "Failed to get joke")
        self.assertIsNotNone(response.json()["value"], "Joke value is null")
        self.assertIsNotNone(response.json()["created_at"], "Joke created date is null")
        assert isinstance(response.json()["created_at"], str)
        assert isinstance(response.json()["categories"], list)
        print("Test passed")


if __name__ == "__main__":
    unittest.main()
