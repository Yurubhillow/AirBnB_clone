import unittest
import models
from models.city import City
from datetime import datetime
import os
from time import sleep


class Test_City_Init(unittest.TestCase):
    """Unit tests for instantiation of the City class."""

    def test_id(self):
        """Tests that the City's id is of str type and is unique"""

        self.assertEqual(str, type(City().id))
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_created_and_updated_at_type(self):
        """Tests that the City's created_at and updated_at are of datetime
        type"""

        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))

    def test_created_and_updated_at_values(self):
        """Tests that the City's created_at and updated_at values differ at
        different times"""

        city1 = City()
        sleep(0.5)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)
        self.assertNotEqual(city1.updated_at, city2.updated_at)

    def test_kwargs(self):
        """Tests that the City's kwargs are correctly handled and updated"""

        kwargs = {"id": "69", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339",
                  "state_id": "420", "name": "Los Angeles"}
        city1 = City(**kwargs)
        self.assertEqual("Los Angeles", city1.name)
        self.assertEqual("420", city1.state_id)
        self.assertEqual("69", city1.id)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         city1.created_at)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         city1.updated_at)

    def test_str(self):
        """Tests that the City's str method is correctly formatted"""

        city1 = City()
        city1.id = "69"
        city1.created_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        city1.updated_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        city1.name = "Los Angeles"
        city1.state_id = "420"
        city1_str = city1.__str__()
        self.assertIn("[City] (69)", city1_str)
        self.assertIn("'id': '69'", city1_str)
        self.assertIn("'name': 'Los Angeles'", city1_str)
        self.assertIn("'state_id': '420'", city1_str)
        self.assertIn("'created_at': datetime.datetime(2021, 2, 17, 22, 46,"
                      " 38, 48339)", city1_str)
        self.assertIn("'updated_at': datetime.datetime(2021, 2, 17, 22, 46,"
                      " 38, 48339)", city1_str)


class Test_City_Save(unittest.TestCase):
    """Unit tests for the save method of the City class."""

    def setUp(self):
        """Sets up the testing environment by creating a City instance"""

        try:
            os.rename("file.json", "temp.json")
        except IOError:
            pass

    def tearDown(self):
        """Removes the testing environment by deleting the created instance"""

        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except IOError:
            pass

    def test_save_valid(self):
        """Tests that the City's save method correctly updates the updated_at
        attribute"""

        city1 = City()
        updated_at = city1.updated_at
        city1.save()
        updated_at2 = city1.updated_at
        self.assertNotEqual(updated_at, updated_at2)

    def test_save_file(self):
        """Tests that the City's save method correctly updates the updated_at
        attribute"""

        city1 = City()
        city1.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_contents(self):
        """Tests that the City's save method correctly updates the updated_at
        attribute"""

        city1 = City()
        city1.save()
        with open("file.json", "r") as f:
            self.assertIn("City." + city1.id, f.read())

    def test_save_arg(self):
        """Tests save command with arguments (shouldn't work)"""

        city = City()
        with self.assertRaises(TypeError):
            city().save("hi")


class Test_City_ToDict(unittest.TestCase):
    """Unit tests for the to_dict method of the City class."""

    def setUp(self):
        """Sets up the testing environment by creating a City instance"""

        try:
            os.rename("file.json", "temp.json")
        except IOError:
            pass

    def tearDown(self):
        """Removes the testing environment by deleting the created instance"""

        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except IOError:
            pass

    def test_to_dict_type_and_class(self):
        """Tests that the City's to_dict method returns a dict type"""

        self.assertEqual(dict, type(City().to_dict()))
        city1 = City()
        self.assertIn("__class__", city1.to_dict())
        self.assertEqual("City", city1.to_dict()["__class__"])

    def test_to_dict_created_and_updated_at(self):
        """Tests that the City's to_dict method correctly adds the created_at
        and updated_at keys"""

        city1 = City()
        self.assertIn("created_at", city1.to_dict())
        self.assertIn("updated_at", city1.to_dict())
        self.assertEqual(str, type(city1.to_dict()["created_at"]))
        self.assertEqual(str, type(city1.to_dict()["updated_at"]))

    def test_to_dict_kwargs(self):
        """Tests that the City's to_dict method correctly adds the kwargs"""

        kwargs = {"id": "69", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339",
                  "state_id": "123", "name": "Los Angeles"}
        city1 = City(**kwargs)
        for key, value in kwargs.items():
            self.assertIn(key, city1.to_dict())
            self.assertEqual(value, city1.to_dict()[key])

    def test_to_dict_return(self):
        """Tests that the City's to_dict method correctly returns a dict"""

        city1 = City()
        self.assertEqual(dict, type(city1.to_dict()))

    def test_to_dict_arg(self):
        """Tests to_dict command with arguments (shouldn't work)"""

        city = City()
        with self.assertRaises(TypeError):
            city().to_dict("hi")
