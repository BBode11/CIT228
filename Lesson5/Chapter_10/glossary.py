print("\t*---------- Hands on #4 ----------*")
import json

def menu():
    selection = int(input("1 -- create file, 2 -- read file, 3 -- add to file, 4 -- quit"))
    while selection != 1 and selection != 2 and selection != 3 and selection != 4:
        print("You made an invalid selection... Please try again.")
        selection = int(input("1 -- create file, 2 -- read file, 3 -- add to file, 4 -- quit"))
    return selection

def create(object):
    overwrite = input("You are about to create a new file, any exisiting data will be erased (q to quit, any key to continue) ")
    if overwrite != "q":
        with open("Chapter_10/glossary.json", "w") as write_file:
            json.dump(object, write_file, indent = 4, sort_keys = True)
            print("glossary.json has been created.")

def append(new_item):
    with open("Chapter_10/glossary.json", "r+") as add_file:
        glossaryDictionary = json.load(add_file)
        glossaryDictionary.update(new_item)
        add_file.seek(0)
        json.dump(glossaryDictionary, add_file, indent = 4, sort_keys = True)
        print("The data has been added to glossary.json")

def read():
    try:
        with open("Chapter_10/glossary.json") as read_file:
            glossaryDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The current file does not exit or cannot be found.")
        print("Please make a different menu selection.")
    else:
        for key, value in glossaryDictionary.items():
            print(key.title(), " definition is ", value)

def get_term():
    term = input("Enter python term: ")
    termname = term.split() [0]
    termname = termname.lower()
    return termname

def get_value():
    glossary_input = input("Enter the python term definition: ")
    return glossary_input

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
choice = menu()
while choice != 4:
    if choice == 1:
        create(glossary)
    elif choice == 2:
        read()
    elif choice == 3:
        pythonTerm = get_term()
        definition = get_value()
        new_dictionary_entry = {pythonTerm : definition}
        append(new_dictionary_entry)
    else:
        print("The option you selected is not available...Please try again.")
    choice = menu()
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

#for k, v in glossary.items():
#    print(k.title())
#    print("\t", v.title())

