print("\t\t***---------- Exercise 9-3 ----------***")
class User:
    def __init__(self, first_name, last_name, username, password, email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.password=password
        self.email=email

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} has a username of {self.username},")
        print(f"a password of {self.password} and an email address of {self.email}")

    def greet_user(self):
        print(f"Welcome back {self.first_name}!")


user1=User("Brandon", "Bode", "BBode11", "password1", "bode11@nmc.edu")
user1.greet_user()
user1.describe_user()
print("")
user2=User("Max", "Bode", "Rottie1", "squirrel", "maxthedog@dogs.net")
user2.greet_user()
user2.describe_user()
print("")
user3=User("Adam", "Sandler", "SNL101", "grownups", "sandyadam@snl.com")
user3.greet_user()
user3.describe_user()


print("\t\t***---------- Exercise 9-5 ----------***")
class User:
    def __init__(self, first_name, last_name, username, password, email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.password=password
        self.email=email
        self.login_attempts=0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} has a username of {self.username},")
        print(f"a password of {self.password} and an email address of {self.email}")

    def greet_user(self):
        print(f"Welcome back {self.first_name}!")

    def login_attempts(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1=User("Brandon", "Bode", "BBode11", "password1", "bode11@nmc.edu")
user1.greet_user()
user1.describe_user()
 
print(f"Number of login attempts for {user1.first_name} is {user1.login_attempts}.\n")

user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Number of login attempts for {user1.first_name} is {user1.login_attempts}.\n")

print("Reset Login Attempts")
user1.reset_login_attempts()
print(f"Number of login attempts for {user1.first_name} is {user1.login_attempts}.\n")



