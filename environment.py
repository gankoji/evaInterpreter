class Environment:
    def __init__(self, record = {}, parent = None):
        self.record = record
        self.parent = parent

    def define(self, name, value):
        self.record[name] = value
        return value

    def assign(name, value):
        self.resolve(name).record[name] = value
        return value

    def lookup(name):
        return self.resolve(name).record[name]

    def resolve(name):
        if (name in self.record.keys()):
            return self

        if self.parent == None:
            raise NameError(f'Sorry, cant find {name} in the environment')

        return self.parent.resolve(name)