class Student:
    def __init__(self):
        self.name = 'Deepak'
        self.age = 20
        self.marks = 100

    def abc(self):
        print('Name of the Student: '+self.name)
        print('Age of the Student: '+str(self.age))
        print('Marks of the Student: '+str(self.marks))

s1 = Student()
s1.abc()
