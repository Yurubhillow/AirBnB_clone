import unittest
import models
from models.user import User
from datetime import datetime
import os
from time import sleep


class Test_User_Init(unittest.TestCase):
    """Unit tests for instantiation of the User class."""

    def test_id(self):
        """Tests that the User's id is of str type and is unique"""

        self.assertEqual(str, type(User().id))
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_and_updated_at_type(self):
        """Tests that the User's created_at and updated_at are of datetime
        type"""

        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))

    def test_created_and_updated_at_values(self):
        """Tests that the User's created_at and updated_at values differ at
        different times"""

        user1 = User()
        sleep(0.5)
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)
        self.assertNotEqual(user1.updated_at, user2.updated_at)

    def test_kwargs(self):
        """Tests that the User's kwargs are correctly handled and updated"""

        kwargs = {"id": "69", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339", "name": "Ian"}
        user1 = User(**kwargs)
        self.assertEqual("Ian", user1.name)
        self.assertEqual("69", user1.id)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         user1.created_at)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         user1.updated_at)

    def test_str(self):
        """Tests that the User's str method is correctly formatted"""

        user1 = User()
        user1.id = "123"
        user1.created_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        user1.updated_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        user1.name = "John"
        user1.email = "ian@goat.com"
        user1.password = "my_pwd"
        user1_str = user1.__str__()
        self.assertIn("[User] (123)", user1_str)
        self.assertIn("'id': '123'", user1_str)
        self.assertIn("'name': 'John'", user1_str)
        self.assertIn("'password': 'my_pwd'", user1_str)
        self.assertIn("'email': 'ian@goat.com'", user1_str)
        self.assertIn("'created_at': datetime.datetime(2021, 2, 17, 22, 46,"
                      " 38, 48339)", user1_str)
        self.assertIn("'updated_at': datetime.datetime(2021, 2, 17, 22, 46,"
                      " 38, 48339)", user1_str)


class Test_User_Save(unittest.TestCase):
    """Unit tests for the save method of the User class."""

    def setUp(self):
        """Sets up the testing environment by creating a User instance"""

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
        """Tests that the User's save method correctly updates the updated_at
        attribute"""

        user1 = User()
        updated_at = user1.updated_at
        user1.save()
        updated_at2 = user1.updated_at
        self.assertNotEqual(updated_at, updated_at2)

    def test_save_file(self):
        """Tests that the User's save method correctly updates the updated_at
        attribute"""

        user1 = User()
        user1.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_contents(self):
        """Tests that the User's save method correctly updates the updated_at
        attribute"""

        user1 = User()
        user1.save()
        with open("file.json", "r") as f:
            self.assertIn("User." + user1.id, f.read())

    def test_save_arg(self):
        """Tests save command with arguments (shouldn't work)"""

        user = User()
        with self.assertRaises(TypeError):
            user().save("hi")


class Test__To_Dict(unittest.TestCase):
    """Unit tests for the to_dict method of the User class."""

    def setUp(self):
        """Sets up the testing environment by creating a User instance"""

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

    def test_user_to_dict_type_and_class(self):
        """Tests that the User's to_dict method returns a dict type"""

        self.assertEqual(dict, type(User().to_dict()))
        user1 = User()
        self.assertIn("__class__", user1.to_dict())
        self.assertEqual("User", user1.to_dict()["__class__"])

    def test_to_dict_created_and_updated_at(self):
        """Tests that the User's to_dict method correctly adds the created_at
        and updated_at keys"""

        user1 = User()
        self.assertIn("created_at", user1.to_dict())
        self.assertIn("updated_at", user1.to_dict())
        self.assertEqual(str, type(user1.to_dict()["created_at"]))
        self.assertEqual(str, type(user1.to_dict()["updated_at"]))

    def test_to_dict_kwargs(self):
        """Tests that the User's to_dict method correctly adds the kwargs"""

        kwargs = {"id": "69", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339", "name": "Ian"}
        user1 = User(**kwargs)
        for key, value in kwargs.items():
            self.assertIn(key, user1.to_dict())
            self.assertEqual(value, user1.to_dict()[key])

    def test_to_dict_return(self):
        """Tests that the User's to_dict method correctly returns a dict"""

        user1 = User()
        self.assertEqual(dict, type(user1.to_dict()))

    def test_to_dict_arg(self):
        """Tests to_dict command with arguments (shouldn't work)"""

        user = User()
        with self.assertRaises(TypeError):
            user().to_dict("hi")
