glossary = {
    "Lists": "A collection of items in a particular order.",
    "Print": "Prints out what is inside of the parentheses.",
    "String": "Series of characters.",
    "Tuples": "List of items that do not change.",
    "Conditionals": "An expression that can be evaluated.",
    "Boolean": "True or false variables.",
    "Len()": "Gives the integer value of the number of characters in a string.",
    "Break": "Used to exit a while loop.",
    "Comments": "Comments in python start with a #.",
    "String Concatentation": "Adding two strings together.",
    }

#print("Lists")
#print("\t", glossary["Lists"])

#print("Print")
#print("\t", glossary["Print"])

#print("String")
#print("\t", glossary["String"])

#print("Tuples")
#print("\t", glossary["Tuples"])

#print("Conditionals")
#print("\t", glossary["Conditionals"])

for k, v in glossary.items():
    print(k.title())
    print("\t", v.title())

