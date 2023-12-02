# write a program to store seven fruits in a list entered by the user

f1 = input("Enter Fruit number 1")

f2 = input("Enter Fruit number 2")

f3 = input("Enter Fruit number 3")

f4 = input("Enter Fruit number 4")

f5 = input("Enter Fruit number 5")

f6 = input("Enter Fruit number 6")

f7 = input("Enter Fruit number 7")


myFruitList = [f1,f2,f3,f4,f5,f6,f7]

print(myFruitList)

# write a program to ccept marks of 6 students and display then in a sorted manner

m1 = int(input("Enter marks for student number 1: "))

m2 = int(input("Enter marks for student number 2: "))

m3 = int(input("Enter marks for student number 3: "))

m4 = int(input("Enter marks for student number 4: "))
    
m5 = int(input("Enter marks for student number 5: "))

m6 = int(input("Enter marks for student number 6: "))

myList = [m1,m2,m3,m4,m5,m6]\
myList.sort()

print(myList)


#check that a tuple cannot be changed in python



a = (2,4,5,3,2)
a[0] = 45



#write a program to sum a list with 4 numbers

a = [2,4,56.7]
print('a[0]+ a[1] + a[2] + a[3]')
print(sum(a))


# write a program to count the number of zeroes in the following tuple:

ls1 = (7,0,8,0,0,9)
print(ls1.count(0))












