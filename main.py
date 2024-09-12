class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Person created")
    
    def say_hello(self):
        print(f"{self.name} says Hello!")

class Student(Person):
    def __init__(self, name, age,average_grade):
        #Person.__init__(self,name, age)
        super().__init__(self,name, age)
        self.average_grade = average_grade
        print("Studet created")
    def study(self):
        print(f"{self.name} studies")
    def say_hello(self):
        print(f"Studet with name:{self.name} says Hello!")
class Teacher(Person):
    def teach(self):
        print(f"{self.name} teaches")
def introduce(person):
    print("Now, a person will say hello")
    person.say_hello()
people_arr=[Student("Tom",15,4.5),Teacher("Katy",37)]

for person in people_arr:
    introduce(person)
p1=Student("Tom",15,4.5)
p1.say_hello()
t1=Teacher("Katy",37)
t1.say_hello()
p1.study()
t1.teach()