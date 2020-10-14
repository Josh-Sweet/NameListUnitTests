import unittest
from NameList import NameList


class NameListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.nameList = NameList()

    def tearDown(self) -> None:
        pass

    def test_name_lookup(self):
        self.nameList.insert("Josh", 21, 1)
        person1 = self.nameList.lookup_person(1)
        self.assertEqual(21, person1.age)
        self.assertEqual("Josh", person1.name)

    def test_for_null(self):
        with self.assertRaises(KeyError):
            self.nameList.lookup_person("You should not be seeing this")

    def test_if_empty(self):
        self.assertFalse(self.nameList.is_empty())
        self.nameList.insert("Josh", 21, 1)
        self.assertTrue(self.nameList.is_empty())

    def test_removal(self):
        self.nameList.insert("Josh", 21, 1)
        self.assertTrue(self.nameList.is_empty())
        self.nameList.remove(1)
        self.assertFalse(self.nameList.is_empty())