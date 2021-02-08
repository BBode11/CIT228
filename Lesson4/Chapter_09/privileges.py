
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