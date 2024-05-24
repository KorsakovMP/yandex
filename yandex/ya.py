class People:
    def __init__(
            self,
            name: str,
            age: int,
            passport: bool,
            weight: int,
            height: float
    ):
        self.nane = name
        self.age = age
        self.passport = passport
        self.weight = weight
        self.height = height

    def get_name(self):
        print(f'Имя человека {self.nane} возраст {self.age}')
        return None

    def is_passport(self):
        if self.passport:
            print(f'У {self.nane} есть паспорт.')
            return self.passport
        print(f'У {self.nane} нет паспорта.')
        return self.passport


class Parent(People):
    def __init__(
            self,
            name: str,
            age: int,
            passport: bool,
            weight: int,
            height: float,
            children: str
    ):
        self.nane = name
        self.age = age
        self.passport = passport
        self.weight = weight
        self.height = height
        self.children = children


misha = People(
    name='Миша',
    age=14,
    passport=False,
    weight=40,
    height=1.70
)
father = Parent(
    name='Папа',
    age=43,
    passport=True,
    weight=88,
    height=1.77,
    children='Миша'
)
p1 = misha.get_name()
p2 = father.get_name()
p3 = misha.is_passport()
p4 = father.is_passport()
print(p1)
