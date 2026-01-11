class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def introduce(self):
        return f"Hi, I'm {self._name}, {self._age} years old."

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        return f"Hi, I'm {self._name}, {self._age} years old, studying {self.major}."

#demonstration
p = Person("your Dad", 50)
s = Student("Daur", 18, "CS")
print(p.introduce())  #encapsulation, inheritance
print(s.introduce())  #polymorphism