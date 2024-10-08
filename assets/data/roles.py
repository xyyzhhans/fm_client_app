import json

# Reading JSON from a file
with open('roles.json', 'r') as file:
    data = json.load(file)
    
for item in data:
    if item.get('RoleCode') in ['bwmd', 'bwms']:
        item['Acc'] = item['Pac'] = 2
        item['Jum'] = 5

    if item.get('RoleCode') in ['bpdc', 'bpdd', 'bpds', 'cdc', 'cdd', 'cds']:
        item['Acc'] = item['Pac'] = 2
        item['Jum'] = 10

    if item.get('RoleCode') in ['cwba', 'cwbs', 'fba', 'fbs', 'fbd', 'ifbd', 'iwba', 'iwbs', 'iwbd', 'wba', 'wbs', 'wbd']:
        item['Acc'] = item['Pac'] = 10
        item['Jum'] = 2
        
    if item.get('RoleCode') in ['ifa', 'ifs', 'iwa', 'iws', 'wa', 'ws']:
        item['Acc'] = item['Pac'] = 10
        item['Jum'] = 2
        
    if item.get('RoleCode') in ['gkd', 'skd', 'sks', 'ska']:
        item['Acc'] = item['Pac'] = 2
        item['Jum'] = 10
        
    if item.get('RoleCode') in ['afa', 'pfa', 'pfs', 'pfd', 'tfs', 'tfa']:
        item['Acc'] = item['Pac'] = 10
        item['Jum'] = 10
        
# Writing the updated JSON back to the file
with open('roles.json', 'w') as file:
    json.dump(data, file, indent=4)
