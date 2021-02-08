from user import User
from privileges import Privileges
from admin import Admin

Darnell = Admin("Darnell", "Jones", "DJ12", "DarJones1", "dj@admin.com")
Darnell.describe_user()
Darnell.privileges.show_privileges()

print("Add privileges")
Darnell_privileges = ["Can add post", "Can delete post", "Can ban user"]
Darnell.privileges.privileges = Darnell_privileges
Darnell.privileges.show_privileges()
