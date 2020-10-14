from Person import Person


class NameList(object):
    def __init__(self):
        self.people = {}

    def is_empty(self):
        if self.people:
            return True
        return False

    def insert(self, name, age, userid):
        self.people[userid] = Person(name, age)

    def remove(self, userid):
        self.people.pop(userid)

    def lookup_person(self, userid):
        return self.people[userid]
