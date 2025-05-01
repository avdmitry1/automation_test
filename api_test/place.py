import requests
import unittest


class TestNewLocation(unittest.TestCase):
    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"
    place_id = None

    def test_1_create_new_location(self):
        post_resource = "/maps/api/place/add/json"
        json = {
            "location": {"lat": -38.383494, "lng": 33.427362},
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park"],
            "website": "http://google.com",
            "language": "French-IN",
        }
        response = requests.post(self.base_url + post_resource + self.key, json=json)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.__class__.place_id = response_json["place_id"]

    def test_2_update_location(self):
        self.assertIsNotNone(
            self.__class__.place_id, "Place ID not set from previous test"
        )
        put_resource = "/maps/api/place/update/json"
        json = {
            "place_id": self.__class__.place_id,
            "address": "100 Shevchenko street, UKR",
            "key": "qaclick123",
        }
        response = requests.put(self.base_url + put_resource + self.key, json=json)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("msg"), "Address successfully updated")

    def test_3_get_location(self):
        self.assertIsNotNone(
            self.__class__.place_id, "Place ID not set from previous test"
        )
        get_resource = "/maps/api/place/get/json"
        params = {
            "place_id": self.__class__.place_id,
            "key": "qaclick123",
        }
        response = requests.get(self.base_url + get_resource + self.key, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("address"), "100 Shevchenko street, UKR")

        print(response.json())

    def test_4_delete_location(self):
        self.assertIsNotNone(
            self.__class__.place_id, "Place ID not set from previous test"
        )
        delete_resource = "/maps/api/place/delete/json"
        json_data = {"place_id": self.__class__.place_id}
        response = requests.delete(
            self.base_url + delete_resource + self.key, json=json_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("status"), "OK")
        print("Location deleted")


if __name__ == "__main__":
    unittest.main()
