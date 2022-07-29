# from asyncio import SendfileNotAvailableError
# from itertools import cycle, product
# from operator import mul
# from os import remove
# from pickle import TRUE
# import re
# from tkinter import Variable
# from unittest import result
# from fastapi import Depends

# from numpy import full_like, intersect1d, true_divide


from platform import python_branch

from numpy import number


age = 17 # declaring and intialising a variable
print(type(age))
print(age)
name = "maram"
print(name)  
single = True

fruits = ["apple" , "banana" , "avocado"]
print(fruits) 
print(type(fruits))
myfruit = fruits[0]
print(myfruit)
myfruit = fruits[1]
print(myfruit)
myfruit = fruits[2]
print(myfruit)


person = {
    "name": "kaoutar" , 
    "age" : 21, 
    "profession": "chomeuse"

}
print(person)

person["profession"]= "insurance agent"
print(person)
person["age"]= "22"
print(person)
person["birth"]= "16/12/2000"
print(person)
del person["age"]
print(person)
animals = ["dog" , "cat", "tiger", "mouse", "horse"]
print(animals)
i=0
myanimal = animals[i]
print(myanimal)
del animals[3]
print(animals)
animals.append('elephant')
print(animals)
exist = "cat" in animals
print(exist)
del animals[3]
if "horse" in animals:
    print("the horse is inside the list0 of animals")
else: 
    print("the horse is not inside the list0 of animals")
if "horse" in animals:
    pass
else: 
    animals.append('horse')

def add(animal):
    if animal in animals:
        pass
    else:
        animals.append (animal)


add("fox")
add("dear")
add("bear")
add("lion")
add("lepord")
print(animals)
x = 4
def fun():
   global x
   x = 7
fun ()
print(x)
numbers = list(range(0,100))
print(numbers)
for x in numbers:
    if x%2 == 0 and x>=90:
        print(x)
myvar= "john"
my_var= "john"
_my_var= "john"
MYVAR= "john"
print(myvar)
print(my_var)
print(_my_var)
print(MYVAR)
x=y=z= "orange"
print(x, y, z)
a = 10
b = 9
if b > a :
    print("b is greater than a")
else :
    print("b is not greater than a")

def maximum(a, b):
    if a>b:
        return a
    else: 
        return b  

print(maximum(5, 2))
print(maximum(2, 7))
print(maximum(8, 9))
print(maximum(4, 2))
numbers = [9, 3, 7]
print(numbers [0])
print(numbers [1])
print(numbers [2])

x = numbers[0] # pour sauvgarder   x=9
numbers[0] = numbers[1]   # numers = [3, 3, 7]
numbers[1] = x            # numers = [3, 9, 7]
print(numbers)
numbers[1] = numbers[2] 
print(numbers)  # numers = [3, 7, 7]
numbers[2] = x
print(numbers)


numbers = [9, 10, 7]
def permuter(i,j):
    x = numbers[i] # pour sauvgarder
    numbers[i] = numbers[j]
    numbers[j] = x

print('--------------')
print(numbers)
permuter(2,1)
print(numbers)

permuter(1,0)
print(numbers)


x = 87
y = x>15 and x==87
print(y)
fruits = ["apple" , "banana" , "avocado"]
print("apple" not in fruits)

thislist = ["apple", "banana", "kiwi", "avocado"]
mylist = thislist.copy()
print(mylist)
i = 3
while i < 10:
    print(i)
    i += 2
i = 1 
while i < 6:
    print(i)
    j = 0
    while j < 3:
        print(10+j)
        j += 1
    if i == 3:
        break
    i += 1
print("start")
i = 0
while i < 6:
  i += 1
  if i == 4:
    continue
  print(i)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
# for x in range(0, 3, 6, 9, 12):

for x in range (0, 13, 3):
    if x == 6:
        continue
    print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


def maximum(a = 0, b =0, c=0):
    if a>=b and a>=c:
        return a
        
    if a<c and b<c: 
        return c
    if b>a and b>c:
        return b
print(maximum(5, 2, 1))
print(maximum(2, 7, 0))
print(maximum(8, 9, 2))
print(maximum())

def say_hello(name = 'kaoutar'):
    return "hello" + ' ' + name

x = say_hello('maram')
print(x)

def one(n):
    if n == 1:
        return 1
    print(n)
    return one(n-1)

output = one(6)
print('the output is ', output)


animals = ["dog" , "cat", "tiger", "mouse", "horse"]
print(animals)

del animals[3]
print(animals)

numbers = [9, 3, 7]
x=numbers[0]
numbers[0] = numbers[1]   
numbers[1] = x
print(numbers)

numbers = [9, 10, 7]
def permuter(i,j):
    x = numbers[i] # pour sauvgarder
    numbers[i] = numbers[j]
    numbers[j] = x

print(numbers)

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

kaoutar = Person("maram", 2, 'unemployed')
kaoutar.speak()
kaoutar.eat()
print(kaoutar.name)

class Person:
    name = None
    age = None
    def __init__(self, name, age):
     self.name = name
     self.age = age
    def say_my_name(self):
        print("hello my name is" + self.name)
p1 = Person("john", "36")        
print(p1.name +' ' + p1.age)
p1.say_my_name()
class employee(Person):
    def __init__(self, name, age, department, is_manager, salary):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager        
        self.salary = salary
employee1 = employee("islam", 56, "marketing", True, 1000000 )   
print(employee1.salary)

employee2 = employee("kaoutar", 60, "facebook", False, 50000000)
print(employee1.age, employee2.age)

# class students:
#     def__init__(self, name, age, gpa, major, university_name)
#         self.name = name
#         self.age = age
#         self.gpa = gpa
#         self.major = major
#         self.university name = university_name
# student1 = student("rachid", 21, 3.5, "computer science", "premier1")
# student2 = student("ahmed", 22, 4.5, "finance", "lettre")
# print(student1.age)

class Employee:
    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
    def add_bonus(self, bonus):
        self.pay += bonus    

        

emp_1 = Employee("corey", "schafer", "44", 5000)

emp_1.add_bonus(500)
print(emp_1.pay)
emp_2 = Employee("test", "user"," 33", 6000)
if emp_1.pay> emp_2.pay:
    print(emp_1.first)
else:
    print(emp_2.first)    



print(emp_1)
print(emp_2)

emp_1.first = "corey"
emp_1.last = "schafer"
emp_1.age = 44
emp_1.pay = 50000


emp_2.first = "test"
emp_2.last = "user"
print(emp_2.age)
emp_2.age = 39
print(emp_2.age)
emp_2.pay = 6000

y = min(2, 4, 7, 9, 0)
print(y)


a = 3
b = 1
print(a, b)
a, b = b, a
print(a, b)



x = abs(-7.25)
print(x)
k=66


print("hello")

try:
    # f = open("./data/myfile.txt",'a')
    f = open("C:/Users/Admin/Desktop/programmation/data/myfile.txt",'a')
    try:
        f.write("\n how are you today")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("it can't open the file cuz it doesn't exist") 

# username = input("enter username:")   
# print("username is:" + username)  

# a = input("enter the first number: ")
# b = input("enter the second number: ")
# c = input("enter the third number: ")

# x = maximum(a, b, c)
# print("the result is : ",x)

def multiplication_or_sum(number1, number2):
        # calculate product of two number
    product = number1*number2

    if product <= 1000:
        # check if product is less then 1000

        return product
    else:
        # product is greater than 1000 calculate sum

        return number1 + number2
result = multiplication_or_sum(20, 30)   
print("the result is", result)

result = multiplication_or_sum(40, 30)
print("the result is", result)

previous_number = 0
for i in range(1, 11):
    x_sum = previous_number + i

    print("Current Number", i, "Previous Number ", previous_number, " Sum: ", x_sum)
    previous_number = i
    
"hello"
animals = ["dog", "elephant", "turkey", "mouse", "fox"]
print(animals[1])
myanimal = animals[1]
# except:
print(myanimal)

class Circle(object):
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)

my_circle = Circle()
x = my_circle.add_radius(5)
print(x)

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
print(b)


d = "ABCDEGH"
print(d[0:3])

e = 'clocrkr1e1c1t'
print(e[::2])

f = "You are wrong"
e = f.upper()
print(e)

name = "Michael Jackson"
k = name.find('el')

print(k)


g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
h = g.find("snow")
n = g.replace("Mary", "Bob")
print(n,h)



L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

L = ["Michael Jackson" , 10.2, 12.5, 8]
L.append(['pop', 10])
print(L)

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
del(A[1])

print('After change:', A)
a = 'A,B,C,D'.split(',')
print(a)

c = 'hard rock music'.split()
print(c)

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

a_list = [1, 'hello', [1, 2, 3] , True]
a_list[1:4]
print(a_list[1:4])

A = [1, 'a'] 
B = [2, 1, 'd']
C = A + B
print(C)

tuple1 = ("disco",10,1.2 )
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
print(tuple2[3:5])
print(len(tuple2))

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(len(genres_tuple)) 
print(genres_tuple[3])
print(genres_tuple[3:6])
print(genres_tuple.index("disco"))

C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
print(C_list)

def func(variable):
    x, y = 12, 15
    if (x&1 == 0):
        result = y
    else:
        result = x
    print(result)        
func(result)    
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict[(0, 1)])
110   
101
100

1100
1111
1100
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
"Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict['Thriller'] )
print(release_year_dict.keys()) 
print(release_year_dict.values()) 
release_year_dict["Graduation"] = "2007"
release_year_dict
print(release_year_dict)
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict
print(release_year_dict)

exist = "The bodyguard" in release_year_dict
print(exist)

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
album_set = set(set1) 
print(album_set)

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)
# convert list0 to set 

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)

A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)
A.add("NSYNC")
print(A)
A.remove("Thriller")
print(A)
exist = "AC/DC" in A
print(exist)

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
intersect1d = album_set1 & album_set2
print(intersect1d)
difference = album_set1.difference(album_set2)  
print(difference)
c = album_set1.intersection(album_set2)   
print(c)
b = album_set1.union(album_set2)
print(b)

l = set(album_set1).issuperset(album_set2)   
print(l)
k = set(album_set2).issubset(album_set1)     
print(k)
n = set({"Back in Black", "AC/DC"}).issubset(album_set1) 
print(n)
d = album_set1.issuperset({"Back in Black", "AC/DC"})   
print(d)



# condition in python

age = 19
if age > 18:
    print("you can enter")
print("move on")    


age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


age = 18
print('-------')
if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

album_year = 1970
album_year = 1983

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


album_year = 1980


if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")    

rating = 8.5
if rating > 8:
    print ("This album is Amazing!")  
else:
    print("this album is ok")      


album_year = 1979

if album_year < 1980 or album_year == 1991 or album_year == 1993:
    print("This album came out in year", album_year)    


    # For loop example
    # The for loop enables you to execute a code block multiple times.
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i]) 

for i in range(0, 8):
    print(i)    

for year in dates:  
    print(year)     

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)    



dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

for i in range(-4, 5):
    print(i)

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'poop']
for Genre in Genres:
    print(Genre)    

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    i = i + 1
    Rating = PlayListRatings[i]
        
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)        

# function
def Mult(a,b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)
print(square(2))
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
print(c1)     


a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
print(c2)  

# def Equation(a = 0,b = 0):

#     c = a + b + 2 * a * b - 1
#     if(c < 0):
#         c = 0 
#     else:
#         c = 5
    
# print(Equation(c))

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)
def div(a, b):
    return(a/b)

class Circle(object):
    

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = 3
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius += r
        return(self.radius)  

my_circle = Circle()
x = my_circle.add_radius(5)
my_circle.color = "white"
print(my_circle.color)

def get_fullname(firstname, lastname):
    full_name = firstname+" " + lastname
    return full_name
firstname = "Selena"
lastname = "Gomez"
full_name = get_fullname(firstname, lastname)
print(full_name)

def build_list(x, y, z):
    A = [x, y, z]
    return A

x = 5
y = 4
z = 3
my_list = build_list(6, 7 , 9)
print(my_list)

def fun(x, y, z):
    result = x + y -z
    return result

Variable = fun(1, 6, 4)

print(Variable)

def fun(a, b):
    if a>b:
        return a - b
    else:
        return a + b    
print(fun(7, 8))             

def fun(N):
    for i in range(N):
        print('hello')
fun(9)


def CheckDuplicate(list0):
    if len(list0) == len(set(list0)):
        return False
    else:
       return True

list0 = "orange", "orange", "apple", "avocado", "browse"
print(CheckDuplicate(list0))

def GetDuplicate(list0):
    count = 0

    for x in list0:
        for y in list0:
            if x == y:
                count +=1
                if count ==2:
                    return x
        count = 0       

print(GetDuplicate(["kiwi","orange", "apple", "orange", "banana"]))

def GetDuplicate(list0):
    print(set(list0))
    for x in set(list0):
        list0.remove(x)
        print(list0)
    return list0[0]    
print(GetDuplicate(["kiwi","orange", "apple", "orange", "banana"]))

def product(number1, number2):
    if number1*number2 <=1000:
        return number1*number2
    else:
    
        return number1+number2
result = product(40, 30)
print(result)            

def fun():
    j=0
    for i in range (0, 11):
        
        print(f"Current Number {i} Previous Number {j} sum {i+j} ")
        j=i
fun()

def fun(word):
    x = word
    for i in x [0::2]:
        print(i)
fun("kaoutar")

list0 = [0, 4, 5, 7, 8, 3]
del list0[4]
print(list0)

def fun(word, n):

    return word[n:]
print(fun("elonmusk", 2))    

def is_same(list0):
    if list0[0] == list0[-1]:
        return True
    else:
        return False
list0 = [10, 20, 40, 70,19]        
print(is_same(list0))    


def numb_list(list0):
    for x in list0:
        if x%5 == 0:
            print(x)
numb_list([10, 30, 55, 60, 47])



def fun(sentence, word):
    return sentence.count(word)
sentence = "Emma is good developer. Emma is a writer"
print(fun(sentence, "good"))    


def fun():
    for i in range(20):
        print(str(i)*i)
fun()        

def palindrome(original_number, reverse_number):
    if original_number == reverse_number:
        return("get palindrome")
    else:
        return("dont get palindrome")  
print(palindrome(451, 451))     


def fun(numbers):
    numbers = str(numbers)
    print(numbers)
    print(numbers[::-1])
    if numbers == numbers[::-1]:
        return True
    else:
        return False
print(fun(1782871))        


def list0(list1, list2):
    new_list = []
    for num in list1:
        if num%2 !=0:
            new_list.append(num)
    for num in list2:
        if num%2 ==0:
            new_list.append(num)
    return new_list        
list1 = [55, 70, 40, 45, 67, 89]
list2 = [90, 30, 43, 21, 44, 80]            

print(list0(list1, list2))


def fun(income):
    if income<=10000:
        return 0
    elif income<=20000:
        return (income-10000)*0.1
    else:
        return (income-20000)*0.2 + 10000*0.1
print(fun(35000))           


def fun():
    for i in range (1, 11):
        line = ""
        for j in range (1, 11):
            line += str(j*i)+" "
        print(line)

    


fun()    

for i in range(10, 0,-1):
    print("*"*i)

A = 2
B = 5
print(A**B)

i = 1
while i<=10:
    print(i)
    i=i+1
    
for i in range(1, 6):
    for j in range(1, 6):
        if j <= i:
            print(j, end= " ")    
    print("") 


def fun(n):
    return n*(n+1)//2
print(fun(10))        

for i in range(1, 10):
    n =2
    result = n*i
    print(result)

def function(list0):
    for n in list0:
        if n>500:
            break
        if n>150:
            continue
        if n%5 ==0:
            print(n)

    
list0 = [12, 75, 150, 180, 145, 525, 50]        
(function(list0))

def function(n):
    n = str(n)
    return len(n)
print(function(78654))


for num in range(-10, 0, 1):
    print(num)


for i in range(5):
    print(i)
    if i>=4:
        print("'done'")
    
def is_prime(n):
    for x in range(2, n):
        if n%x==0:
            return False
    return True           


for i in range(2, 100):
    if is_prime(i):
        print(i)



if True:
    print("koko")
if False:
    print("lll")


list0 = [0,1]

for num in range(8):
    result= list0[-1] + list0[-2]
    list0.append(result)


for x in list0:
    print(x)
def factor(n):
    if n == 1:
        return 1
    return n*factor(n-1)

print(factor(3))


def happy(number):
    history= []
    output = number
    while True:
        output = str(output) # '82'
        result = 0
        for c in output:   # '8'    '2'
            x = int(c)     # 8       2
            result += x**2  # 64     4
        output = result     #68
        if output == 1:
            print(f"{history} {output}")
            return True
        if output in history :
            print(f"{history} {output}")
            return False
        else:
            history.append(output)  # [82, 68]
    return None


print(happy(19))

def canFinish(numcourses, prerequisites):
    for i in range(numcourses):
        finish = True
        Depends= None
        for p in prerequisites:
            if i == p [0]:
                finish = False
                Depends = p[1]
        if finish == True:
            continue
        if finish == False:
            for p in prerequisites:
                if Depends == p [0]:
                    return False
    
    return True

print(canFinish(2, [[1,0]]))             

def two_argument(name, age):
    print(name, age)

two_argument("kaoutar", 45) 
                

def func1(*var):
    for i in var:
        print(i)
func1(20, 40, 60)
func1(80, 100)
func1(70, 11)

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
print(calculation(40, 10))    


def calculation(a, b):

    return a + b, a - b

# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)
#create function with defaut argument

def show_employee(name, salary = 9000):
    print("name:", name, "salary:", salary)
show_employee("ben",12000)
show_employee("jess")

def outer_fun(a = 2, b = 3):
    # square = a**2
    a = a**2
    def addition(a, b):
        return a + b
        #call inner function from outer function
    add = addition(a, b)
    return add + 5    
result = outer_fun(5, 10)
print(result)

# create a recursive function

def display_student(name, age):
    print(name, age)
display_student("emma", 44)    
show_student = display_student
show_student("emma", 44)

def mylist(numbers):
    for i in numbers:
        print(i)

    

mylist(range(4, 30,2))


x = [37, 88, 73, 22, 99 ]
print(min(x))


list1 = [12, 33, 55, 36, 98]
list2 = [12, 45, 76, 12, 36]
res = list()


odd_elements = list1[1::2]
print(odd_elements)

even_elements = list2[::2]
print(even_elements)

res.extend(odd_elements)
res.extend(even_elements)
print(res)



a = 'A,B,C,D'.split(',')
print(a)

c = 'hard rock'.split()
print(c)


code = "ply2t3h4o5n6i7c8"
print(code.replace("l", "").replace("2", ""))
print(code[0:1] + code[2:3] + code [4:5])
print(code[0::2].upper())
print(code[1::2][::-2])

words = 'i saw a cat jump over the moon and into the clouds'
var = words.split()
print(var)
print(len(var))
print(var[3:8:2])

new_words = "i saw a cow fly over the gates and into the forest "
s1 = slice (3, 12, 2)
print(s1)

name = "Goegie" ; grade = "A+++"
print("the student's name is {} and the grade is {}". format(name ,grade))

animals = ["lions", "zebras", "elephants"]
safari = "i saw {}, {} and {}!"
print(safari.format(animals[0].upper(), animals[1].capitalize(), animals[2].upper()))
print(safari.format(*animals))

num = "200"
print(eval (num) + 10) 


print("%d * %d = %d" %(10, 20, (10*20 )))

print("%d * %d = %d" %(10, 20, (10*20)))
print("%d*%d = %f" %(5, 3, (5/3)))
print("%d*%d = %.2f" %(5, 3, (5/3)))
print("%d*%d = %d" %(5, 3, (5/3)))


word = "awesome"
x = " the length of this word {} is {}". format(word, len(word))
print(x)

y = "days left are {num: .5f}". format (num = 300/9  )
print(y)

num = 300/9 
z = f"days left are {num : .4f}"
print(z)

p1 = "python" ; p2 = "older" 
g = f"""This is a docstring that uses {p1} 3.6 and can't be used for {p2} versions of {p1}""" .replace ("\n", "").upper()
print(g)

# lists and range

num = [10, 30, 40]
num [0] = "hello"
print (num)
n = list (range(0, 20, 4))
m = list(range(-70, 80, 10))
print(m)

nest = [[1, 2 ,3], [5 ,6, 7]]
print(nest[0])

new = [list(range(5)), list(range(5, 10))]
print(new)

print(nest + new )


print(type(new))

number1 = [99, 55, 88]
number1.append(100)

number1.sort()
number1.insert(2, 200)
print(number1)
number1.pop()


print(number1)
# pop : remove the last element 

items = ["car", "robot", "ball"]
print(items)
items[0] = "ps4"
print(items)
items.append(number1)
print(items)
items[3]. insert(3, ["hey!"])
print(items)

# tuple and bluit it in functions
tuple = 40, 60, 30, 22
print(tuple)

# MyList = [90, 21, 20, 44]
# o= tuple(MyList)
# print(o)

numbers = [10, 20, 30, 40]
print(eval("{0}+ {1}+ {0}+{3}". format(*numbers)))
