def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

        #10-10
def find_words(filename, search):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower().count(search)
        print(f"The word, {searchWord}, occured {words} times in the {filename} file. " )


filenames = ['Chapter_10/babe_ruth.txt', 'Chapter_10/don_zimmer.txt', 'Chapter_10/kate_miller-wilson.txt']
for filename in filenames:
    count_words(filename)

searchWord = input("What common word would you like to search for within the files? ")
for filename in filenames:
    find_words(filename, searchWord)
