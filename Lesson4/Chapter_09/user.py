
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