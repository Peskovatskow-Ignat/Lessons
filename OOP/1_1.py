class Student():
    def __init__(self, name, point):
        self.n = name
        self.p = point
        self.c = None

    def output(self):
        print(self.n)
        print(self.p)
        print(self.c)

    def set_course(self, name_course):
        self.c = name_course

Kolyn = Student('Сашка', 99)

Kolyn.set_course('Шляпка')

Kolyn.output()