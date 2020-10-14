from Person import Person


# Contains a list of names of people
class NameList(object):
    def __init__(self):
        self.people = {}

    # Checks if the list of people is empty
    def is_empty(self):
        if self.people:
            return True
        return False

    # Inserts and new person into the list
    def insert(self, name, age, userid, phoneNumber):
        self.people[userid] = Person(name, age, phoneNumber)

    # Removes a person from the list
    def remove(self, userid):
        self.people.pop(userid)

    # Looks up a person in the list. Returns an empty person object if they aren't there.
    def lookup_person(self, userid):
        try:
            return self.people[userid]
        except KeyError:
            return Person("", 0, 0)

    # Checks to see if multiple people have the same phone number, which should not happen.
    def check_correctness(self):
        # There is a faster way to do this, but for simplicity it is done this way.
        for userid1, person1 in self.people.items():
            for userid2, person2 in self.people.items():
                if userid1 == userid2:
                    pass
                elif person1.phoneNumber == person2.phoneNumber:
                    return False

        return True
