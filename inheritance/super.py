class Parent:
    def __init__(self, name):
        print("calling init method of parent class", name)


class Parent1:
    def __init__(self, name):
        print("calling init method of parent1 class", name)


class Child(Parent, Parent1):
    def __init__(self):
        print("calling init method of child")
        #super().__init__('Poonam')
        Parent.__init__(self, 'Poonam')
        Parent1.__init__(self, 'Archu')



child = Child()
print(Child.__mro__)
