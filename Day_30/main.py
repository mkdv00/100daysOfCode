# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "val"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = ["apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "val"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("File does not exist.")
# except KeyError as error_message:
#     print(f"That key: {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("There is an error that I made")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
