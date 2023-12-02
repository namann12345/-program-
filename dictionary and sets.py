myDict = {
    "Fast": "In a Quick Manner",
    "Harry" : "A coder",
    "Marks" : [1,2,5],
    "anotherdict":{'harry': 'player'}
}

str
#print(myDict['Fast'])
#print(myDict['Harry'])
myDict['Marks'] = [45,78]
print(myDict['Marks'])    
print(myDict['anotherdict']['harry'])


myDict = {
    "Fast": "In a Quick Manner",
    "Harry" : "A coder",
    "Marks" : [1,2,5],
    "anotherdict":{'harry' : 'player'},
    1:2
}  

#dictionary methods

print(list(myDict.keys())) # prints the keys of the dictionary
print(myDict.values()) # prints the keys of the dictionary
print(myDict.items()) # prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "lovish": "friend",
    "palak": "friend",
    "divya": "friend",
    "harry": "a dancer",
}

myDict.update(updateDict) # updates the dictionary by adding key value pairs from updateDict
print(myDict)



print(myDict.get("harry")) # prints value associated with key "harry"
print(myDict["harry"])  # prints value associated with key "harry"

# the difference between .get and[] syntax in dictionaries 
print(myDict.get("harry2")) # returns none as harry2 is not present in the dictionary
print(myDict["harry2"])  # throws an error as harry2 is not present in the doctionary










