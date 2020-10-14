import unittest
from NameList import NameList


class NameListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.nameList = NameList()

    def tearDown(self) -> None:
        pass

    # Test that a name can be looked up
    def test_name_lookup(self):
        self.nameList.insert("Josh", 21, 1, 12345)
        person = self.nameList.lookup_person(1)
        self.assertEqual(21, person.age)
        self.assertEqual("Josh", person.name)

    # Test that the list was ever properly created.
    # This can also silently test if a list is properly deleted as well.
    def test_for_null(self):
        self.nameList.lookup_person(1)
        self.assertTrue(self.nameList.lookup_person(1).name == "")

    # Test that a list is empty, and will not remain empty after being performed on.
    def test_if_empty(self):
        self.assertFalse(self.nameList.is_empty())
        self.nameList.insert("Josh", 21, 1, 12345)
        self.assertTrue(self.nameList.is_empty())

    # Test that an item can be removed
    def test_removal(self):
        self.nameList.insert("Josh", 21, 1, 12345)
        self.nameList.insert("David", 29, 2, 6789)

        self.nameList.remove(1)

        person1 = self.nameList.lookup_person(1)
        person2 = self.nameList.lookup_person(2)

        self.assertTrue(person1.name == "")
        self.assertTrue(person2.name == "David")
        self.assertTrue(person2.age == 29)

    # Test that an item can be replaced. Realistically this shouldn't be done however.
    def test_replacement(self):
        self.nameList.insert("Josh", 21, 1, 12345)
        self.nameList.insert("David", 29, 1, 6789)

        person1 = self.nameList.lookup_person(1)

        self.assertEqual(29, person1.age)
        self.assertEqual("David", person1.name)

    # Test to make sure the function to check if two people have the same phone number works.
    def test_correctness(self):
        self.nameList.insert("Josh", 21, 1, 12345)
        self.nameList.insert("David", 29, 2, 6789)

        self.assertTrue(self.nameList.check_correctness())

        self.nameList.insert("David", 29, 2, 12345)

        self.assertFalse(self.nameList.check_correctness())
