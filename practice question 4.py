# write a program to create a dictionary of hindi words eith values as their english translation provide user with an option to look it up!

myDict = {
    "pankha" :"fan",
    "dabba" : "box",
    "vastu" : "item"
}
print("option are", myDict.keys())
a = input("emter the hindi word\n")
#print("the meaning of your word is:", myDict[a])

#below line will not throw an error if the key is not present in the dictionary
print("the meaning of your word is:", myDict.get(a))

#write a program to input eight numbers from the user and display all the unique numbers(once)

num1 = int(input("enter number 1\n"))
num2 = int(input("enter number 2\n"))
num3 = int(input("enter number 3\n"))
num4 = int(input("enter number 4\n"))
num5 = int(input("enter number 5\n"))
num6 = int(input("enter number 6\n"))
num7 = int(input("enter number 7\n"))
num8 = int(input("enter number 8\n"))

s = {num1,num2,num3,num4,num5,num6,num7,num8}
print(s)


# can we have a set with 18(int) and "18"(str) as a values in it?

s = {18,"18"}
print(s)
