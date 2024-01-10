print("Welcome to the Madlib Game!")
print("This is an interactive game where you fill in the blanks to create a funny story.")
print("Let's get started!\n")

def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()
