def maximum(a = 0, b =0, c=0):
    if a>=b and a>=c:
        return a
        
    if a<c and b<c: 
        return c
    if b>a and b>c:
        return b

class Person:
    name = ""
    age = None
    profession = None
    def __init__(self, name, age, profession):
        self.name =name
        self.age =age
        self.profession =profession

    def speak(self):
        print("i'am speaking")
    def eat(self):
        print("i'am eating")