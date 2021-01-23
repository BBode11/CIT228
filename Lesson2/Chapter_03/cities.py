print("---------- Exercise 3-10 ----------\n")
citiesList = ["Grand Rapids", "Lansing", "Detroit", "Big Rapids", "Traverse City", "Alpena", "Atlanta", "Midland", "Bay City", "Holland", "Escanaba", "Marquette"]
#example of f-string
message = f"I would like to live just outside of {citiesList[4].title()} one day."
print(message)
print("Original List: ", citiesList, "\n")

#example of append *adds to end of list* and insert
citiesList.append("Fenton")
citiesList.insert(0, "Lake City")
print("List After Append: ", citiesList, "\n")

#example of deletion *deletes from list*
del citiesList[-1]
citiesList.pop()
citiesList.remove("Lake City")
print("List After Deletions: ", citiesList, "\n")

#example of sorted, sort, and reverse
citiesList.sort()
print("List Sorted in Alphbetical Order : ", citiesList, "\n")

print("List with Temporary Sort: ", sorted(citiesList), "\n")

citiesList.reverse()
print("List Sorted in Reverse: ", citiesList, "\n")

#Example using len function
print("There are", len(citiesList), "in the final list.")
