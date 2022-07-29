Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutar"
Name = "kaoutr"
Name = "hanae" 
FirstName = "Hanae "
lastName = "kallat"
FullName = FirstName + lastName




ageKaoutar = 21
ageHassane = 30
# print ('ageKaoutar ',ageKaoutar)
# print ('ageHassane ',ageHassane)
stock = ageKaoutar
ageKaoutar = ageHassane
ageHassane = stock
# print ('ageKaoutar ',ageKaoutar)
# print ('ageHassane ',ageHassane)

a = [1, 42, 5, 9]
# print (a[2])
stock = a[1]
a[1] = a[2]
a[2] =stock
# [1, 5, 42, 9]
# print (a[3])
stock = a[2]
a[2] = a[3]
a[3] =stock



# print(a) 
Name = input ("what's your Name ")
age = input ("hi "+ Name +"! what's your age ")
age = int(age)
minor = int(age) < 18
print(type(minor))
print(type(age))
print(type(Name))

quit()
if minor :
    print ("you are a minor")
elif int(age) < 21:
    print("you are major but you can't drink")
else:
    print("You are a major and allowed to drink")