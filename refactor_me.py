class Parent:

    def get_first_name(self, fullname):
        return fullname.split(' ')[0]

    def hey(self, fullname):
        print(f'Hello {self.get_first_name(fullname)}')


class Child(Parent):
    MAX_AGE = 18

    def __init__(self, age=18):  # No age is the same behavior that > 18
        self.age = age

    def hey(self, fullname):
        if not self.is_adult():
            print(f"What's up {self.get_first_name(fullname)}?")
        else:
            super().hey(fullname)

    def is_adult(self):  # age = 18 case is missing from original code
        return self.age and self.age >= self.MAX_AGE


if __name__ == '__main__':

    a = Parent()
    b = Child()
    c = Child(14)
    a.hey('Alfredo Topete Escamilla')
    b.hey('Alfredo Topete Escamilla')
    c.hey('Alfredo Topete Escamilla')
