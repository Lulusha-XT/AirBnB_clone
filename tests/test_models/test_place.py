#!/usr/bin/python3

"""Module for test place"""

from unittest import TestCase

from models.place import Place

from models.base_model import BaseModel

from .test_class import TestClassDocumentation





class TestState(TestCase):

    """Test cases for Place"""



    def test_code_review(self):

        """Test documentation and pep8"""

        t = TestClassDocumentation(self, Place)

        t.documentation()

        t.pep8(['models/place.py', 'tests/test_models/test_place.py'])



    def test_class(self):

        """Validate the types of the attributes an class"""

        with self.subTest(msg='Inheritance'):

            self.assertTrue(issubclass(Place, BaseModel))



        with self.subTest(msg='Attributes'):

            self.assertIsInstance(Place.city_id, str)

            self.assertIsInstance(Place.user_id, str)

            self.assertIsInstance(Place.name, str)

            self.assertIsInstance(Place.description, str)

            self.assertIsInstance(Place.number_rooms, int)

            self.assertIsInstance(Place.number_bathrooms, int)

            self.assertIsInstance(Place.max_guest, int)

            self.assertIsInstance(Place.price_by_night, int)

            self.assertIsInstance(Place.latitude, float)

            self.assertIsInstance(Place.longitude, float)

            self.assertIsInstance(Place.amenity_ids, list)
