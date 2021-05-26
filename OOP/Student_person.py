from Person import Person


class Student(Person):
    def __init__(self, id, first_name, last_name, carrer):
        #Person.__init__(self, id, first_name, last_name)
        super().__init__(id, first_name, last_name)
        self.carrer = carrer


student_one = Student(200, 'Asaf', 'Aznar', 'ISC')
print(student_one)
