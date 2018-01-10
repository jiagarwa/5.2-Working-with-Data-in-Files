#imports for json and Pandas
import pandas as pd
import json
from pandas.io.json import json_normalize

#load json data from source file using open function
json_data = json.load((open('data/world_bank_projects.json')))

#apply json normalize on the column 'mjtheme_namecode' and get distinct value combination for each record
json_norm = json_normalize(json_data, 'mjtheme_namecode',sep= ",")

#apply groupby method on dataframe with column 'name' and chain it with count() method
projectname = json_norm.groupby('name').count()

#get the top 10 common project name using 'nlargest' method on name and ocnver it into a new Dataframe "result' 
result = pd.DataFrame(projectname.nlargest(10, 'code'))
print(result)
