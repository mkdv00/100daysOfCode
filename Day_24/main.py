import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'my_file.txt')

# with open(my_file) as file:
#     contents = file.read()
#     print(contents)

with open(my_file, mode="w") as file:
    file.write("New text.")
