class Environment:
    def __init__(self, record = {}, parent = None):
        self.record = record
        self.parent = parent

    def print(self):
        print(f"Here's an environment. Local level: {self.record}")
        parent = self.parent
        while parent:
            print(parent.record)
            parent = parent.parent

    def define(self, name, value):
        self.record[name] = value
        return value

    def assign(self, name, value):
        self.resolve(name).record[name] = value
        return value

    def lookup(self, name):
        return self.resolve(name).record[name]

    def resolve(self, name):
        if (name in self.record.keys()):
            print(f"Found {name} at this level: {self.record}")
            return self

        print(f"Failed to find {name} at this level: {self.record}. Going to parent")
        if self.parent == None:
            raise NameError(f'Sorry, cant find {name} in the environment')

        return self.parent.resolve(name)