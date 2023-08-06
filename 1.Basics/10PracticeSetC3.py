# Display name of User after wishing the Day
name = input("Enter your name")
print ( "Good Morning " +name )

# Write the template for name and date

Template = ('''Dear <|NAME|>  
            Congratulation,You are Selected!
            Date : <|DATE|>
''')
name = input("Enter your name")
date = input("Enter Date")
Template.replace("<|NAME|>",name)
Template.replace("<|DATE|>",date)
print(Template)

#Check the Double space in the string

Text = input('This is   a test  set.')
Text.find("  ")
print(Text.find)

#Single Space Detection

Text = input('This is   a test  set.')
Text.find(" ")
print(Text.find)

# Use the Escape sequence

Set = ('''This is a (tab space)\t and this is a next line \n  and we are using \ and \ for double quote we are using \\are we good\\ ''')
print(Set)