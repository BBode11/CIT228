print("\t\t***---------- Exercise 9-7 ----------***")
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

class Admin(User):
    def __init__(self, first_name, last_name, username, password, email):
        super().__init__(first_name, last_name, username, password, email)
        self.privileges = []

    def show_privileges(self):
        print("\tPrivileges: ")
        for privilege in self.privileges:
            print("\t\t", privilege)

Darnell = Admin("Darnell", "Jones", "DJ12", "DarJones1", "dj@admin.com")
Darnell.describe_user()

Darnell.privileges = ["Can add post", "Can delete post", "Can ban user"]
Darnell.show_privileges()

print("\n\t\t***---------- Exercise 9-8 ----------***")
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

class Admin(User):
    def __init__(self, first_name, last_name, username, password, email):
        super().__init__(first_name, last_name, username, password, email)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\tPrivileges: ")
        if self.privileges:
           for privilege in self.privileges:
            print("\t\t", privilege)
        else:
            print("\t\tUser has no privileges")

Darnell = Admin("Darnell", "Jones", "DJ12", "DarJones1", "dj@admin.com")
Darnell.describe_user()
Darnell.privileges.show_privileges()

print("Add privileges")
Darnell_privileges = ["Can add post", "Can delete post", "Can ban user"]
Darnell.privileges.privileges = Darnell_privileges
Darnell.privileges.show_privileges()
