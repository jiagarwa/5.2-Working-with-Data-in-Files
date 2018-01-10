#imports for json and Pandas
import pandas as pd
import json
from pandas.io.json import json_normalize

#load json data from source file using open function
json_data = json.load((open('data/world_bank_projects.json')))

#apply json normalize on the column 'mjtheme_namecode' and get distinct value combination for each record
json_norm = json_normalize(json_data, 'mjtheme_namecode',sep= ",")

# Few record has a blank name, to fill this we will fill them using itertuples
name_dict = {}
for row in json_norm.itertuples():
    if row[2] != '':
        name_dict[row[1]] = row[2]
name_dict

# Fill in missing names using the name dictionary
for row in json_norm.itertuples():
    if row[2] == '':
        json_norm.set_value(row[0], 'name', name_dict[row[1]])

# additionl Check to make sure there are no more missing entries
print('Number of missing name entries:', len(json_norm[json_norm['name'] == '']))
print(json_norm)

