import pandas as pd
import json

data = json.load(open('15Games.json'))

#m = pd.json_normalize(data,['resultSets',''],['resultSets','rowSet'],[['resultSets','headers'],['resultSets','name']])


#m = pd.json_normalize(data)

#df_out = pd.json_normalize(data['resultSets']).explode('rowSet').reset_index(drop=True)

#df_out = pd.concat([df_out.drop('resultSets', axis=1), pd.DataFrame(df_out['rowSet'].to_list())], axis=1)

#print(df_out)
#df = pd.DataFrame(data["resource"])

#print(data["resultSets"][0])

#print(data["resultSets"][0]["headers"])

print(data["resultSets"][0]["rowSet"])
#print(m)
