import pandas as pd
import json
from datetime import datetime
  

d3 = datetime.today().strftime("%m/%d/%Y 00:00:00")

df = pd.read_json("scheduleLeagueV2_1.json")

dt_from_str = lambda dt: datetime.strptime(dt, '%d-%b-%Y')

with open('scheduleLeagueV2_1.json') as f:
    nbaSched = json.load(f)

#mySchd = nbaSched['leagueSchedule']['gameDates'][0]['games']
mySchd = nbaSched['leagueSchedule']['gameDates']

# key,myvalue = 'gameDate','09/30/2022 00:00:00'
# for k, v in mySchd.items():
#         #if v['gameDate'] == '09/30/2022 00:00:00':
#         print(k)
#         print(v)

for id, info in nbaSched.items():
    print(id)
    for k in info:
        if k == 'gameDates':
            for i in info[k]:
                if i['gameDate'] == d3: # '03/08/2023 00:00:00':
                    df = pd.json_normalize(i['games'])
                    break
        print(k)
        #print(k, info[k])
#homeTeam.teamId homeTeam.teamName	awayTeam.teamId	awayTeam.teamName


#print( mySchd )

print(df)

#df.to_csv('TodaysNBA_Sched.csv')

df = df[['gameId','gameCode','homeTeam.teamId','homeTeam.teamName','awayTeam.teamId','awayTeam.teamName'] ]

print(df)

""" 
for k, v in d.items():
        if v['make'] == make and v['model'] == model:
            return k

key,value = 'gameDate','09/30/2022 00:00:00'
dictList = [ myV for myDict, myV in mySchd if myDict== value ]
print(dictList) """




#print( nbaSched['leagueSchedule']['gameDates'][0] )



##############################
"""df = pd.json_normalize(mySchd)
print ( df )
 
df['gameDate'] = pd.to_datetime(df['gameDate'])
print ( df.head() )

temp = (df.gameDate == d3)

todaysGames = df.loc[temp]
print (df.loc[temp])


myList = pd.json_normalize(
    todaysGames, 
    record_path =['games'] 
)

print(myList) """
#######################

#print( pd.today() )
#print( df.gameDate = pd.Timestamp  )
#print( df.query("gameDate == '04/05/2023 00:00:00'", inplace=True ) )



# for sub_dict in mySchd:
#     for key, val in sub_dict.items():
#         if start_date <= dt_from_str(key) <= end_date:
#             new_dict[key] = val

#print(df['leagueSchedule']['gameDates'][0])

# df.head()

# myStr ="Were testing this ORA-1244 check this issue"

# print(myStr.find("ORA"))
# print ( myStr[myStr.find("ORA"):])