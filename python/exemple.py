from cgi import print_form
import numbers
from re import I, S, X
from sqlite3 import ProgrammingError
from this import d
from tkinter import OFF
from traceback import print_tb
from unicodedata import name
from xml.dom.minidom import Element
from click import progressbar
from numpy import append, indices


if 1 > 2:
    print("Five is greater than two!") 
print("Five is greater than two!") 

text='my sister said "jjjuuu "'




def fun (my_list):
    return my_list[1]


my_li = [2, 5, 7,9]
print(fun(my_li))


def fun2 (numbers):
    indice = numbers[0] 
    return numbers[indice]

numbers = [2, 4, 8, 9, 0, 6]
print(fun2(numbers))


def fun3 (age):
    if age < 18: 
       print ("fuckOFF")
    else :
        print("come in")
fun3(16)        
fun3(77)

def fun4 (list1, number):
    if number in list1:
        print("true")
    else :
        print ("false")    
list7 = [2, 3, 4, 9, 0]       
fun4(list7, 9)

def add (list1, number):
    list1.append(number)
    return list1


# list = [2, 3, 4, 9, 0]     
# add(list, 7)  
# add(list, 98)  
# print(list)


def function (list):
    # list.reverse()    list = list.reverse
    return list
    
# list = [43, 56, 67, 22, 46]

# function(list)
# print(list)    

    

def swap (numbers):
    x = numbers[0]
    numbers[0] = numbers[-1]
    numbers[-1] = x
    print(numbers)

# list = [99, 70, 56, 34]
# swap(list)    





number = 37
number = str(number)
first = (number[0])
last = (number[1])
first = int(first)
last = int(last)
add = first + last 
print(add)


number =37
print(number//10+number%10)


def find (numbers):
    for i in range(len(numbers)):
        if 3==numbers[i]:
            return i

# list = [0, 8, 5, 7, 8, 7, 3,5,43]
# print(find(list))

company = {
"name" : "tesla",
"number of employees" : 50000,
"age" : 2003,


}
company["salary"] = 150000

print(company["number of employees"] * company["salary"]) 



firm = {
"name" : "spaceX",
"number of employees": 40000,
"age" : "2002",
"salary" : 180000
}
print(company)

def fun(company, firm):
    if company["salary"] * company["number of employees"] > firm ["salary"] * company["number of employees"]:
        return company ["name"]
    else:
        return firm ["name"]  
print(fun(company, firm))          
def merge(company1, company2):
    new_company = {}
    new_company["name"] =   company1["name"] + company2["name"]
    new_company["number of employees"] = company1["number of employees"] + company2["number of employees"]
    new_company["salary"] = (company1["salary"] + company2["salary"])/2
    return new_company

print(merge(company, firm))




my_list = [45, 23, 12, 90, 33, 21]
Element = my_list.pop(4)
print(my_list)
my_list.insert(2, Element)
print(my_list)
my_list.append(Element)
print(my_list)




def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()        

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


my_list = [{
    "name" : "john",
    "age": 56
},

{
    "name": "amma",
    "age": 29

}]

my_list.append({"name":"mohamed", "age": 58})
my_list[0]["gender"]= "male"

# my_list = my_list*2
# del my_list[1]
# x = my_list.values("name")

my_list2= []

for person in my_list:

    if person["age"]>50:
        my_list2.append(person)
print(my_list2)        

        # print(person["name"])




# print(my_list[0].values())
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


my_function_with_args("kaoutar", "hello")

def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(5, 7))    

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

obj = MyClass()
print(obj.variable)   #attribute
obj.function() #method

class NumberHolder:
    def __init__(self, number):
       self.number = number

    #    def returnNumber(self):
    #        return self.number
    def __repr__(self):
        return "number :"+str(self.number)

obj = NumberHolder(7)
# print(obj.returnNumber()) #Prints '7'
print(obj.number) #Prints '7'
obj = NumberHolder(8)
# print(obj.returnNumber()) #Prints '7'
print(obj) #Prints '7'

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    def __repr__(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    def __init__(self, name, color, kind, value):

        self.name = name  
        self.color = color
        self.kind = kind
        self.value = value


# your code goes here

car1 = Vehicle("maram", "red", "bmw",1000000)
car2 = Vehicle("ko", "blue", "audi", 120000)
# test code
print(car1)
print(car2.description())

def fun(X):
    
    if 3< X <5:
        print ("X between 3 and 5")
    else:
        print(None)    
fun(X)        

# item1 = "phone"
# item1_price = 1000
# item1_quantity = 5
# item1_price_total = item1_price*item1_quantity

# print(type(item1))  
# print(type(item1_price))

#creation of the class: part 1
#instantiate some objects of this class: part 2
#creating an object or creating an instance its the same thing


# # when you go ahead and create those functions inside classes those are called methods
# item1 = Item()

# item1.name = "phone"
# item1.price = 100
# item1.quantity = 5     #each one of this attributes are assigned to one instance 


# item2 = Item()
# item2.name = "laptop"
# item2.price = 1000
# item2.quantity = 3     #each one of this attributes are assigned to one instance 
# #understand how we can create methods and execute them on our instances 
# print(item2.calculate_totale_price(item2.price, item2.quantity))

# # random_str = "aaa"
# # print(random_str.upper())


# 0 == False  # => True
# 1 == True   # => True
# 2 == True   # => False
# -5 != False # => True
# print("Hello, World", end="!")
li = [4, 5, 3]
x = li.append(1)
print(x)


var = "house"; var2 = "cinema" ; var3 = "temple"
"o" in var
"z" not in var

MyList = [90, 21, 20, 44]
o= tuple(MyList)
print(o)

tup5 = "cat", "cat", "cat", "cat","dog", "elephant", True
print(tup5.count("cat"))
print(tup5.index(True))        #position of the element
tup1 = 40, 22, 89, 44, 12
print(sum(tup1*2))
print(max(tup1))
print(min(tup1))
print(tuple(sorted(tup1)))

# tup5[0] = "dog"
# print(tup5)

d1 = {}
# type(d1)
d1["A"] = 10
d1["B"] = 20
d1["C"] = 50
print(d1)

toys = {"robot" : "$25.99", "car": "$45.88"}
print(toys)
d1.update(toys)
d1["A"] = 120
print(d1)

d1.pop("A")
print(d1)

#convert into list or  tuple for indexing
list(d1.values())[2:4]
class Item:
    def __init__(self, name):
        print(f"An instance created:{name}")
        
    def calculate_totale_price(self, x = 7, y= 6):
        return (x * y)  

my_item = Item("pc")
print(my_item.calculate_totale_price())

list(d1.values())[2:4]
print(d1)

menu = [("chips", 2.4), ("soup", 1.4)]
print(dict(menu))
maze = {"k1":d1,
        "k2": [10, 20, 30],
        "k3":("tuple!", [1, 2, {"k4":["a", "b", "catch me" ]}])}
print(maze)     

print(maze["k3"][1][2]["k4"][2])

# task1 add all dictionary values

toys = {"robot": "$40.0", "car": "$25", "iroman": "$12" }
print(list(toys.values())[0][1])
# numero= (int(eval(list(toys.values())[0][1:])) + eval(list(toys.values())[1][1:]) + eval(list(toys.values())[2][1:]))
numero= (float(list(toys.values())[0][1:]) + float(list(toys.values())[1][1:]) + float(list(toys.values())[2][1:]))
print(numero)
#task2 use comparaison operator in a list 
questions = [10 != 4, 50 == 50, 90 == 10, "c" in  ("a", "b", "c"), 100 !=100]
print(questions)

# task3 len key value with comparaison operator 
films = {"k1" :"blade runner 2049", "k2": "matrix", "k3": "ninja scroll"}
print(len(films["k1"]) >len(films["k2"]) < len(films["k3"]))
#task4 update dictionary 
life_stages = {0 : "embryo", 1: "fetus", 2: "baby", 3: "infant", 4: "teen"}
midlife = {5:"adult", 6: "big kid!"}
life_stages.update(midlife)
print(life_stages)

#task5 : add all values from list 

nest1 = [(1, 2, 3), {"k1": [30, 1, 300, 2, 77], "k2": [10, 20, 30]}, ["a", "500" ,"c"]]

k0 = nest1[0][2]
print(k0)
k1 = sorted (nest1[1]["k1"])[-1]
print(k1)
# 
k2 = nest1[1]["k2"][2]
print(k2)

k3 = eval(nest1[2][1])
print(k3)

print(float(k0 + k1 + k2 + k3))