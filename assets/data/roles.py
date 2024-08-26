import json

# Reading JSON from a file
with open('roles.json', 'r') as file:
    data = json.load(file)
    
for item in data:
    if item.get('RoleCode') in ['bwmd', 'bwms']:
        item['Acc'] = item['Pac'] = 2
        item['Jum'] = 2

    if item.get('RoleCode') in ['bpdc', 'bpdd', 'bpds', 'cdc', 'cdd', 'cds']:
        item['Acc'] = item['Pac'] = 2
        item['Jum'] = 10

# Writing the updated JSON back to the file
with open('roles.json', 'w') as file:
    json.dump(data, file, indent=4)
