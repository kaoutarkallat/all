from itertools import product
import numbers


def even(name = 'interview'):
    n = len(name)
    for i in range(n):
        if i%2 == 0:
            print(name[i])


even('pynative')

text = "table"
subtext = text[1:]
text = subtext
print(subtext)

def first_last_name(numbers):
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False

numbers1 = [10, 24, 46, 33, 10]
numbers2 = [45, 66, 78, 87, 44]
print(first_last_name(numbers1),first_last_name(numbers2))

numbers = [10, 25, 46, 33, 20]
for x in numbers:
    if x%5 == 0:
        print(x)
    
4567654

product="bottle of water"
n = product.count("t")
print(n) 

list1 = [10, 20, 25, 30, 35]
list2 = [10, 20, 25, 30, 35]
new_list = []
for x in list1:
    if x%2 == 1:
        new_list.append(x)
for x in list2:
    if x%2 == 0:
        new_list.append(x)



print(new_list)

level = 2020
text = str(level)
print("laptop", end=' ')
print("keyboard")

A = "Thriller is the sixth studio album"
B = A.upper()
print(B)

A = 'Micheal Jackson is the best'
B = A.replace('Micheal', 'Janet')
B = 'Janet jackson is the best'

