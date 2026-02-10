from collections import Counter
class PersonInfo:
    def __init__(self, fio, age, *deps):
        self.fio = fio
        self.age = age
        self.deps = deps
    def short_name(self):
       return f"{self.fio[self.fio.find(' ')+1:]} {self.fio[:1]}."
    def path_deps(self):
        road = self.deps[0]
        for i in self.deps[1:]:
            road += f" --> {i}"
        return road
    def new_salary(self):
        d = sum([i[1] for i in Counter((''.join(self.deps))).most_common(3)])
        salary = 1337 * self.age * d
        return salary

