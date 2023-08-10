"""Defines unittests for models/base_model.py file."""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
import os
from time import sleep


class Test_Base_Model_Innit(unittest.TestCase):
    """unittests for instantiation of the Basemodel class."""

    def test_id(self):
        """Tests that the BaseModels id is of str type and is unique"""

        self.assertEqual(str, type(BaseModel().id))
        Bmodel1 = BaseModel()
        Bmodel2 = BaseModel()
        self.assertNotEqual(Bmodel1.id, Bmodel2.id)

    def test_created_and_updated_at_type(self):
        """Tests that the BaseModels created_at and updated_at are of datetime
        type """

        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_created_and_updated_at_values(self):
        """Tests that the BaseModels created_at and updated_at values differ at
        different times"""

        Bmodel1 = BaseModel()
        sleep(0.5)
        Bmodel2 = BaseModel()
        self.assertNotEqual(Bmodel1.created_at, Bmodel2.created_at)
        self.assertNotEqual(Bmodel1.updated_at, Bmodel2.updated_at)

    def test_kwargs(self):
        """Tests that the BaseModels kwargs are correctly handled and updated
        """

        kwargs = {"id": "123", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339",
                  "name": "Ian"}
        Bmodel1 = BaseModel(**kwargs)
        self.assertEqual("Ian", Bmodel1.name)
        self.assertEqual("123", Bmodel1.id)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         Bmodel1.created_at)
        self.assertEqual(datetime(2021, 2, 17, 22, 46, 38, 48339),
                         Bmodel1.updated_at)

    def test_str(self):
        """Tests that the BaseModels str method is correctly formatted"""

        Bmodel1 = BaseModel()
        Bmodel1.id = "123"
        Bmodel1.created_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        Bmodel1.updated_at = datetime(2021, 2, 17, 22, 46, 38, 48339)
        Bmodel1.name = "Ian"
        Bmodel1.my_number = 89
        Bmodel1_str = Bmodel1.__str__()
        self.assertIn("[BaseModel] (123)", Bmodel1_str)
        self.assertIn("'id': '123'", Bmodel1_str)
        self.assertIn("'name': 'Ian'", Bmodel1_str)
        self.assertIn("'my_number': 89", Bmodel1_str)
        self.assertIn("'created_at': datetime.datetime(2021, 2, 17, 22,"
                      " 46, 38, 48339)", Bmodel1_str)
        self.assertIn("'updated_at': datetime.datetime(2021, 2, 17, 22,"
                      " 46, 38, 48339)", Bmodel1_str)


class Test_Base_Model_save(unittest.TestCase):
    """unittests for the save method of the BaseModel class."""

    def setUp(self):
        """Sets up the testing environment by creating a BaseModel instance"""

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
        """Tests that the BaseModels save method correctly updates the
        updated_at attribute
        """
        Bmodel1 = BaseModel()
        updated_at = Bmodel1.updated_at
        Bmodel1.save()
        updated_at2 = Bmodel1.updated_at
        self.assertNotEqual(updated_at, updated_at2)

    def test_save_file(self):
        """Tests that the BaseModels save method correctly updates the
        updated_at attribute
        """
        Bmodel1 = BaseModel()
        Bmodel1.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_contents(self):
        """Tests that the BaseModels save method correctly updates the
        updated_at attribute
        """
        Bmodel1 = BaseModel()
        Bmodel1.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + Bmodel1.id, f.read())

    def test_save_arg(self):
        """Tests save command with arguments(shouldnt work)"""

        Bmodel = BaseModel()
        with self.assertRaises(TypeError):
            Bmodel().save("hi")


class Test_Base_Model_to_dict(unittest.TestCase):
    """unittests for the to_dict method of the BaseModel class."""

    def setUp(self):
        """Sets up the testing environment by creating a BaseModel instance"""

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

    def test_to_dict_type(self):
        """Tests that the BaseModels to_dict method returns a dict type"""

        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_to_dict_class(self):
        """Tests that the BaseModels to_dict method correctly adds the
        __class__ key
        """

        Bmodel1 = BaseModel()
        self.assertIn("__class__", Bmodel1.to_dict())
        self.assertEqual("BaseModel", Bmodel1.to_dict()["__class__"])

    def test_to_dict_created_and_updated_at(self):
        """Tests that the BaseModels to_dict method correctly adds the
        created_at and updated_at keys
        """

        Bmodel1 = BaseModel()
        self.assertIn("created_at", Bmodel1.to_dict())
        self.assertIn("updated_at", Bmodel1.to_dict())
        self.assertEqual(str, type(Bmodel1.to_dict()["created_at"]))
        self.assertEqual(str, type(Bmodel1.to_dict()["updated_at"]))

    def test_to_dict_kwargs(self):
        """Tests that the BaseModels to_dict method correctly adds the kwargs
        """

        kwargs = {"id": "123", "created_at": "2021-02-17T22:46:38.048339",
                  "updated_at": "2021-02-17T22:46:38.048339",
                  "name": "Ian"}
        Bmodel1 = BaseModel(**kwargs)
        for key, value in kwargs.items():
            self.assertIn(key, Bmodel1.to_dict())
            self.assertEqual(value, Bmodel1.to_dict()[key])

    def test_to_dict_return(self):
        """Tests that the BaseModels to_dict method correctly returns a dict
        """

        Bmodel1 = BaseModel()
        self.assertEqual(dict, type(Bmodel1.to_dict()))

    def test_to_dict_arg(self):
        """Tests to_dict command with arguments(shouldnt work)"""

        Bmodel = BaseModel()
        with self.assertRaises(TypeError):
            Bmodel().to_dict("hi")
