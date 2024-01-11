print("Welcome to the Madlib Game!")
print("This is an interactive game where you fill in the blanks to create a funny story.")
print("Let's get started!\n")

def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_template(template):
    # Use regular expressions to find placeholders
    import re
    pattern = r'{([^}]*)}'  # Matches anything between curly braces
    matches = re.findall(pattern, template)

    # Replace placeholders with {} in the stripped template
    stripped_template = re.sub(pattern, '{}', template)

    return stripped_template, tuple(matches)

def merge(template, values):
    return template.format(*values)