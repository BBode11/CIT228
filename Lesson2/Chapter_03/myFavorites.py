foods = ["Buffalo Dip", "Pizza", "Chicken Tenders", "Mac and Cheese", "Hamburger", "Sweet Potatoes", "French Fries"]
print(foods)

numbers = [1, 5, 6, 12, 24, 32]
print(numbers)

movies = ["Step Brothers", "The Shawshank Redemption", "Tombstone"]
print(movies)

combo = ["Buffalo Dip", "Pizza", 1, 5, "Step Brothers", "Tombstone"]
print(combo)

print(foods[-1])
print("Num 2=", numbers[1])
print("Num 6=", numbers[-1])
print("Num 4=", numbers[-3])

print("All movies=", movies)

print("First food=", foods[0])
print("First number=", numbers[0])
print("First movie=", movies[0] + "\n")

print("------------------Hands on 2---------------------\n")
movies.append("The Sandlot")
print("Added movie: ", movies)
#add movie to the end

numbers.insert(3, 18)
print("Added numbers: ", numbers)
#number inserted at the 3 position

foods.insert(5, "Coney Dog")
print("Added food: ", foods)
#insert new food at the 5th position

numbers.pop()
print("Deleted last number: ", numbers)
#Deletes number from the end

numbers.pop(2)
print("Deleted number at 2 position: ", numbers)
#deletes number  from the 2 position

print("------------------Hands on 3---------------------\n")
movies.sort()
print("Sorted movies: ", movies)
#sorts movies into alphbetical order

foods.sort()
print("Sorted foods: ", foods)
#Sorts foods into alphbetical order

print("Temp sorted list: ", sorted(numbers))
print("Original list: ", numbers)
#sorted numbers

movies.reverse()
print("Reverse movies order: ", movies)
#reveresed order of movies