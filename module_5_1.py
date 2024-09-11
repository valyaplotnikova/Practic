class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            res = [i for i in range(1, new_floor+1)]
            print(*res, sep='\n')
        else:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Этажи', 7)
h1.go_to(5)
h2.go_to(10)
h3.go_to(7)
h3.go_to(17)
