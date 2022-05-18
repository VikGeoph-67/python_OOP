"""
Множественное наследование
Один потомок наследует сразу от нескольких родителей
"""

class Parent1:
    def __init__(self):
        super().__init__()
        self.smart='smart'
        self.hair_color='light'

class Parent2:
    def __init__(self):
        super().__init__()
        self.pretty='pretty'
        self.hair_color='black'

class Children(Parent1,Parent2):
    def __init__(self):
        super().__init__()

    def traints(self):
        print(self.pretty)
        print(self.smart)
        print(self.hair_color)

child=Children()
child.traints()



