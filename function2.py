 
def name(**name):
    print(type(name))
    print("Hello,", name["fname"],
          name["mname"], name["lname"])


name(mname = "buchanan", lname = "Barnes", fname = "james")
