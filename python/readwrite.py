


file1 = open("resources/data/example1.txt","r")


line1 = file1.readline()
print(line1)

line2 = file1.readline()

print(line2)

line3 = file1.readline()
print(line3)

print("hna ghtbda for loop")
for line in file1:
    print(line)

file2 = open("resources/data/example2.txt","w")

file2.write("i'm gonna be a computer scientist this year\n")
file2.write("this year i'm gonna be studying for my master's degree")


