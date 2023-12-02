c#print('hello world')

a = 'naman'
b = 345
c = 45.32
d = False
d = None
#printing the variables
print(a)
print(b)
print(c)
print(d)

#printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))


a = 3
b = 4
print("the value of a+b is ",a+b)
print("the value of a-b is ",a-b)
print("the value of a*b is ",a*b)
print("the value of a/b is ",a/b)

#assignment operators

a = 34
a +=12
print(a)

b = 34
b -=12
print(b)

c = 34
c *=12
print(c)

d = 34
d /=12
print(d)

#comparison operators

a = (4<=7)
b = (4>=7)
c = (4<7)
d = (4>7)
e = (4==7)
f = (4!=7)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#logical operators
bool1 = True
bool2 = False
print("the value of bool1 and bool2 is ",(bool1 and bool2))
print("the value of bool1 and bool2 is ",(bool1 or bool2))
print("the value of not bool2 is ",(not bool2))

a = "3534"
a = int(a)
print(type(a))
print(a+5)

a = input("enter your name")
print(type(a))


a = 20
b = 30
print("the sum of a and b is",a+b)

a = 458
b = 15
print(a%b)


a = input("enter first number:")
b = input("enter second number:")
a = int(a)
b = int(b)
avg = (a+b)/2
print("the average of a and b is",avg)

#string
a = 34
b = "naman"
print(a,b)
print(type(b))

greeting = "good morning,"
name = "naman"
print(type(name))
c = greeting + name
print(c)

name = "naman"
#print(name[1:5])
#print(name[:5])
print(name[1:5:2])

name = "namanisgood"
d = name[0::3]
print(d)

story = "once upon a time there was a programmer name naman who uploaded python course with notes"

#string functions
print(len(story))
print(story.endswith("notes"))
print(story.count("c"))
print(story.capitalize())
print(story.find("naman"))
print(story.replace("naman","codewithnaman"))

story = "naman is good.\nhe is very good"
print(story)

a = input("enter your name\n")
print("good afternoon," + name)



letter = '''Dear <|NAME|>,
greetings from abc coding house. i am happy to tell you about your selection you are selected !
you are selected!
have a great day ahead!
thanks and regards,
bill
date: <|DATE|>
'''

name = input("enter your name\n")
date = input("enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>", date)
print(letter)


st = "this is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)

letter = "dear naman,this python course is nice! thanks!"
print(letter)

formatted_letter = "dear harry,\n\tthis python course is nice!\nthanks!"
print(formatted_letter)

#list and tuples


#create a list using[]
a = [1,2,4,56,6]

#print the list using print() function 
print(a)

#access using index using a[0],a[1],a[2]
print(a[2])

#change the value of list using 
a[0] = 98
print(a)

#we can create a list with items of different types

c = [45,"naman",False,6.9]
print(c)

#list slicing
friends = ["abhishek","aman","arti","palak","pankaj",45]
print(friends[0:4])
print(friends[-4:])

l1 = [1,8,7,2,21,15]
#l1.sort()# sorts the list
#l1.reverse() # reverses the list
#l1.append(45) # adds at the end of the list
#l1.insert(2,544) # inserts 544 at index 2
#l1.pop(2) # removes element at index 2 
#l1.remove(21) # removes 21 from the list  
print(l1)


# creating a tuple using()
t = (1,2,4,5)

#t1 = () #empty tuple
# t1 = (1) # wrong way to declare a tuple with single element 
t1 = (1,) # tuple with single element 
print(t1)

#printng the elements of a tuple
#print(t[0])


# cannot update the values of a tuple
#t[0] = 34 


#count method

t = (1,2,4,5,4,1,2,1,1)
print(t.count(1))

# index method

print(t.index(5))


#practice question 
f1 = input("eneter fruit number 1")
f2 = input("eneter fruit number 2")
f3 = input("eneter fruit number 3")
f4 = input("eneter fruit number 4")
f5 = input("eneter fruit number 5")
f6 = input("eneter fruit number 6")
f7 = input("eneter fruit number 7")


myFruitList = [f1,f2,f3,f4,f5,f6,f7]
print(myFruitList)


m1 = int(input("enter marks for student number 1:"))
m2 = int(input("enter marks for student number 2:"))
m3 = int(input("enter marks for student number 3:"))
m4 = int(input("enter marks for student number 4:"))
m5 = int(input("enter marks for student number 5:"))
m6 = int(input("enter marks for student number 6:"))

myList = [m1,m2,m3,m4,m5,m6]
myList.sort()
print(myList)


a = (2,4,5,3,2)
a[0] = 45
