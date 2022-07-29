a = [1, 5, 16, 4, -7, 9, 2, 4]
somme = 1 + 5 + 6 + 4 -7
print (somme)
somme = a[0] + a[1] + a[2] + a[3] + a[4] 
print (somme)

Sum = 0
for element in a:
    if element % 2== 1:
        Sum = Sum + element
print ("Sum ", Sum)
moyenne = Sum/len(a)
print ("moyenne ",moyenne)
N = len(a)
print (N)
