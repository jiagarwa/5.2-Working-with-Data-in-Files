import pandas as pd
import json

# read json file as Pandas dataframe
json_df = pd.read_json('data/world_bank_projects.json', orient = 'columns') 

#apply groupby method on dataframe and chain it with count() method
countries = json_df.groupby('countrycode').count()

#get the 5 largest count of '_id' column using 'nlargest' method on countries and ocnver it into a new Dataframe "result' 
result_df = pd.DataFrame(countries.nlargest(5,'_id'))

#print all the  row and first column of result dataframe
result = result_df.iloc[:,0]
print(result)
