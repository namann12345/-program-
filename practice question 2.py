

# write a python program to display a user entered name followed by good agternoon using input() function.

name = input("Enter your name")
print("Good Afternoon," + name)


# write a proram to fill in letter template given below with name and date.
letter = '''Dear <|Name|>,
Greetings from ABC coding house. I am happy to tell you about your selection
you are selected!
Have a great day ahead!
thanks and regards,
Bill
Date: <|Date|>
'''

name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)


# write a program to detect double spaces in a string

st = "this is a string with double    spaes"

st = st.replace("  "," ")
print(st)  
# write a program to format the folloeing letter using escape sequence characters.

letter = "Dear Harry, this python course is nice! thanks!"
print(letter)

formatted_letter = "Dear Harry,\n\tThis python course is nice!\nthanks!"
print(formatted_letter)
