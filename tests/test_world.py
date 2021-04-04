#!/usr/bin/env python3

import unittest
from world_class import World
from world_class import Languages


class WorldTestCase(unittest.TestCase):
    def setUp(self):
        ...

    def test_world(self):
        lang_es = Languages().find_by_code(value="es")
        lang_gn = Languages().find_by_code(value="gn")
        lang_en = Languages().find_by_code(value="en")

        country = World().find_by_code(value="ar")
        self.assertTrue(country.name == "Argentina")
        self.assertTrue(54 in country.phone)
        self.assertEqual([lang_es, lang_gn], country.languages)

        country = World().find_by_code(value="es")
        self.assertTrue(country.name == "Spain")
        self.assertTrue(34 in country.phone)
        self.assertTrue(lang_es in country.languages)


    def test_languages(self):
        lang = Languages().find_by_code(value="en")
        self.assertTrue(lang.name == "English")
        self.assertEqual("en", lang.code)
        self.assertFalse(lang.rtl)

        lang = Languages().find_by_code(value="es")
        self.assertTrue(lang.name == "Spanish")
        self.assertTrue(lang.native == "Español")
        self.assertEqual("es", lang.code)
        self.assertFalse(lang.rtl)

        lang = Languages().find_by_code(value="ur")
        self.assertTrue(lang.name == "Urdu")
        self.assertTrue(lang.rtl)
