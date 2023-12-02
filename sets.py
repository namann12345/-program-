a = {1,3,4,5,1}
print(type(a))
print(a)

# important: this syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

#an empty set can be created using the below syntax:
b = set()
print(type(b))

# adding values to an empty sets 
b.add(4)
b.add(5)
b.add(5)
b.add(5)# adding a value repeatedly does not change a set 
b.add((4,5,6))

#b.add({4:5}) # cannot and list or dictionary to sets 
print(b)

print(len(b)) # prints the length of this set 

b.remove(5)# removes 5 from set b 
b.remove(15)# throws an error while trying to remove 15 (which is not present in the set)
print(b)
