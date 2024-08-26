import json

# Reading JSON from a file
with open('roles.json', 'r') as file:
    data = json.load(file)

# Writing the updated JSON back to the file
with open('roles.json', 'w') as file:
    json.dump(data, file, indent=4)
