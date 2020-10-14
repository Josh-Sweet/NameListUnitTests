class NameList(object):
    def __init__(self):
        self.people = {}

    def is_empty(self):
        if self.people:
            return True
        return False

    def insert(self, name, age):
        self.people[name] = age

    def lookup_age(self, name):
        return self.people[name]
