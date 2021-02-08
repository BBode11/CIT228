from user import User
from privileges import Privileges
class Admin(User):
    def __init__(self, first_name, last_name, username, password, email):
        super().__init__(first_name, last_name, username, password, email)
        self.privileges = Privileges()

 