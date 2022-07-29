from typing import Counter


def fun (binary='10000010001'):
    Counter = 0
    stock = []
    for x in binary:
        if x == '1' :
            stock.append(Counter)
            Counter = 0
        else:
            Counter +=1  
    print(stock)
    return max(stock)
print(fun())

def fun(list,k):
    return list[-k:] +list[0:-k]
list1 = [5, 6, 3, 1, 9]
print(list1)
print(fun(list1,3))    

def fun(list = [9, 3, 9, 7, 3]):
    store = {}
    for x in list:
        if x not in store:
            store[x] = True
        else:
            del store[x]

    for key in store:
        return key
            
print(fun()
)

def fun (start=10, end=70, jump=30):
    return (end - start-1)//jump + 1 

print(fun())

