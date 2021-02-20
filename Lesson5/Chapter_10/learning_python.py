print("\t*---------- Exercise 10-2 ----------*")
filename = "Chapter_10/learning_python.txt"

print("Reading and printing a text file.\n")
with open(filename) as textFile:
    text = textFile.read()
print(text)

print("\nReading and looping over lines in text file.")
with open(filename) as textFile:
    for line in textFile:
        print(line.rstrip())

print("\nReading and placing text file into list.")
with open(filename) as textFile:
    lines = textFile.readlines()
for line in lines:
    print(line.rstrip())

print("\t*---------- Exercise 10-2 ----------*")
with open(filename) as textFile:
    lines = textFile.readlines()
for line in lines:
    line = line.rstrip()
    print(line.replace("python", "C#"))