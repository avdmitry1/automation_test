import requests
import unittest


class TestRandomJoke(unittest.TestCase):
    URL = "https://api.chucknorris.io/jokes/random"
    URL_BY_CATEGORY = "https://api.chucknorris.io/jokes/random?category="

    def test_random_joke_creation(self):
        response = requests.get(self.URL)
        joke = response.json()
        self.assertEqual(response.status_code, 200, "Failed to get joke")
        self.assertIsNotNone(joke["value"], "Joke value is null")
        self.assertIsNotNone(joke["created_at"], "Joke created date is null")
        self.assertIsInstance(joke["created_at"], str)
        self.assertIsInstance(joke["categories"], list)

    def test_random_joke_creation_by_category(self):
        category = "sport"
        response = requests.get(self.URL_BY_CATEGORY + category)
        self.assertEqual(response.status_code, 200, "Failed to get joke")
        self.assertEqual(response.json()["categories"][0], category)


if __name__ == "__main__":
    unittest.main()
