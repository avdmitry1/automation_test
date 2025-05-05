import unittest


class testType(unittest.TestCase):
    first_name = "Eric"
    second_name = "Garcia"

    def test_new_value(self):
        self.__class__.first_name = "Jason"
        self.__class__.second_name = "Momoa"
        self.assertIsInstance(self.__class__.first_name, str)
        self.assertIsInstance(self.__class__.second_name, str)
        self.assertIsNot(self.__class__.first_name, self.__class__.second_name)
        self.assertNotIsInstance(self.__class__.first_name, int)
        self.assertNotIsInstance(self.__class__.second_name, float)

    
if __name__ == "__main__":
    unittest.main()
