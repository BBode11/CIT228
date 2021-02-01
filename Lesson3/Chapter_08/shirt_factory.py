print("*------------- 8-3 -------------*\n")
def make_shirt(shirt_size, shirt_text):
    print(f"The size of the shirt is {shirt_size}.")
    print(f"The text printed on the shirt is '{shirt_text}'.")

make_shirt("Large", "Bubba Gump Shrimp")


print("*------------- 8-4 -------------*\n")
def make_shirt(shirt_size='Large', shirt_text='I love python'):
    print(f"\nThe size of the shirt is {shirt_size}.")
    print(f"The text printed on the shirt is '{shirt_text}'.")

make_shirt()
make_shirt(shirt_size='Medium')
make_shirt("Small", "Texas Pete Hot Sauce")