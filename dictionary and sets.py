myDict = {
    "Fast": "In a Quick Manner",
    "Harry" : "A coder",
    "Marks" : [1,2,5],
    "anotherdict":{'naman': 'player'}
}

str
#print(myDict['Fast'])
#print(myDict['naman'])
myDict['Marks'] = [45,78]
print(myDict['Marks'])    
print(myDict['anotherdict']['naman'])


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



print(myDict.get("naman")) # prints value associated with key "naman"
print(myDict["naman"])  # prints value associated with key "naman"

# the difference between .get and[] syntax in dictionaries 
print(myDict.get("naman2")) # returns none as naman2 is not present in the dictionary
print(myDict["naman2"])  # throws an error as naman2 is not present in the doctionary










