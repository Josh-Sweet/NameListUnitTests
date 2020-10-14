import unittest

from NameList import NameList


class NameListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.nameList = NameList()

    def tearDown(self) -> None:
        pass

    def test_name_lookup(self):
        self.nameList.insert("Josh", 21)
        age = self.nameList.lookup_age("Josh")
        self.assertEqual(21, age)

    def test_for_null(self):
        with self.assertRaises(KeyError):
            self.nameList.lookup_age("You should not be seeing this")

    def test_if_empty(self):
        self.assertTrue(self.nameList.is_empty())
