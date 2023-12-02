 #b = "Harry's" --> #use this if you have single quotes in your strings 
#b = 'Harry"s'
b = '''Harry"s and
       Harry's'''

print(b)
#print(type(b))
 

greeting = "Good Morning,"
name = "Harry"
#print(type(name))
c = (greeting + name)
print(c)


#concatenating two strings

name = "Harry"
print(name[4])
# name[3] = "d" --> does not work

#print(name[0:4])
#print(name[:4]) # is same as name [0:4]
#print(name[1:]) # is same as name [1:5]


c = name[-4:-1]# is same is name[1:4]
print(c)

#slicing with skip value

name = "HarryIsGood"
d = name[0::2] 
print(d)


story = "once upon a time there was a youtuber named Harry who uploaded python course with notes"

print(story[0:5])

#string functions
print(len(story))
print(story.endswith("notes"))
print(story.count("a"))
print(story.capitalize())
print(story.find("upon"))
print(story.replace ("Harry", "codewithHary"))


story = "Harry is good.\nHe\tis very good"
print(story)


 


