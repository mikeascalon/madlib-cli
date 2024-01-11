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

if __name__ == "__main__":
    template_file_path = "../assets/dark_and_stormy_night_template.txt"
  

    # Read the template from the file
    template_content = read_template(template_file_path)
   

    # Parse the template into usable parts
    stripped_template, placeholders = parse_template(template_content)
    
    # Collect user inputs for each placeholder
    user_inputs = []
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder}): ")
        print(user_input)
        # user_inputs[placeholder] = user_input
        user_inputs.append(user_input)

    # Populate the template with user inputs
    madlib_result = stripped_template
    for placeholder, value in user_inputs.items():
        madlib_result = madlib_result.replace("{" + placeholder + "}", value)

    # Print the final Madlib story
    print("\nMadlib Result:\n", madlib_result)