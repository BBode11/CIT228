import random
prompt = "Would you like to keep playing?"
prompt += " Enter 'q' to end the game."
#problems = int(input("How many math problems would you like to practice?"))
keepPlaying = ""
numberCorrect = 0
while keepPlaying != "q":
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer == yourAnswer:
        print("Great job, you answered correctly!")
        numbernumberCorrect += 1
    else:
        print("Oops, the correct answer is ",correctAnswer)
        keepPlaying = input(prompt)

print("You answered ", numberCorrect, "questions correctly!")
print("Thanks for playing!")