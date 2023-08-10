import unittest
import models
from models.state import State
from datetime import datetime
import os
from time import sleep


class Test_State_Init(unittest.TestCase):
    """Unit tests for instantiation of the State class."""

    def test_id(self):
        """Tests that the State's id is of str type and is unique"""

        self.assertEqual(str, type(State().id))
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_created_and_updated_at_type(self):
        """Tests that the State's created_at and updated_at are of datetime
        type"""

        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))

    def test_created_and_updated_at_values(self):
        """Tests that the State's created_at and updated_at values differ at
        different times"""

        state1 = State()
        sleep(0.5)
        state2 = State()
        self.assertNotEqual(state1.created_at, state2.created_at)
        self.assertNotEqual(state1.updated_at, state2.updated_at)

    def test_kwargs(self):
        """Tests that the State's kwargs are correctly handled and updated"""

        kwargs = {"id": "69", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339", "name": "Texas"}
        state1 = State(**kwargs)
        self.assertEqual("Texas", state1.name)
        self.assertEqual("69", state1.id)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         state1.created_at)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         state1.updated_at)

    def test_str(self):
        """Tests that the State's str method is correctly formatted"""

        state1 = State()
        state1.id = "69"
        state1.created_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        state1.updated_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        state1.name = "Texas"
        state1_str = state1.__str__()
        self.assertIn("[State] (69)", state1_str)
        self.assertIn("'id': '69'", state1_str)
        self.assertIn("'name': 'Texas'", state1_str)
        self.assertIn("'created_at': datetime.datetime(2021, 2, 17, 22, 46,"
                      " 38, 48339)", state1_str)
        self.assertIn("'updated_at': datetime.datetime(2021, 2, 17, 22, 46,"
                      " 38, 48339)", state1_str)


class Test_State_Save(unittest.TestCase):
    """Unit tests for the save method of the State class."""

    def setUp(self):
        """Sets up the testing environment by creating a State instance"""

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
        """Tests that the State's save method correctly updates the updated_at
        attribute"""

        state1 = State()
        updated_at = state1.updated_at
        state1.save()
        updated_at2 = state1.updated_at
        self.assertNotEqual(updated_at, updated_at2)

    def test_save_file(self):
        """Tests that the State's save method correctly updates the updated_at
        attribute"""

        state1 = State()
        state1.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_contents(self):
        """Tests that the State's save method correctly updates the updated_at
        attribute"""

        state1 = State()
        state1.save()
        with open("file.json", "r") as f:
            self.assertIn("State." + state1.id, f.read())

    def test_save_arg(self):
        """Tests save command with arguments (shouldn't work)"""

        state = State()
        with self.assertRaises(TypeError):
            state().save("hi")


class Test_State_To_Dict(unittest.TestCase):
    """Unit tests for the to_dict method of the State class."""

    def setUp(self):
        """Sets up the testing environment by creating a State instance"""

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
        """Tests that the State's to_dict method returns a dict type"""

        self.assertEqual(dict, type(State().to_dict()))
        state1 = State()
        self.assertIn("__class__", state1.to_dict())
        self.assertEqual("State", state1.to_dict()["__class__"])

    def test_to_dict_created_and_updated_at(self):
        """Tests that the State's to_dict method correctly adds the created_at
        and updated_at keys"""

        state1 = State()
        self.assertIn("created_at", state1.to_dict())
        self.assertIn("updated_at", state1.to_dict())
        self.assertEqual(str, type(state1.to_dict()["created_at"]))
        self.assertEqual(str, type(state1.to_dict()["updated_at"]))

    def test_to_dict_kwargs(self):
        """Tests that the State's to_dict method correctly adds the kwargs"""

        kwargs = {"id": "69", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339", "name": "Texas"}
        state1 = State(**kwargs)
        for key, value in kwargs.items():
            self.assertIn(key, state1.to_dict())
            self.assertEqual(value, state1.to_dict()[key])

    def test_to_dict_return(self):
        """Tests that the State's to_dict method correctly returns a dict"""

        state1 = State()
        self.assertEqual(dict, type(state1.to_dict()))

    def test_to_dict_arg(self):
        """Tests to_dict command with arguments (shouldn't work)"""

        state = State()
        with self.assertRaises(TypeError):
            state().to_dict("hi")
