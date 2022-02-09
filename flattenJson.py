import pandas as pd
import json
import csv

data = json.load(open('15Games.json'))

with open('pt_data1.csv', 'w', newline='', encoding='utf-8') as pt_data1:
    csvwriter = csv.writer(pt_data1)
    csvwriter.writerow( data["resultSets"][0]["headers"] )
    #csvwriter.writerow( data["resultSets"][0]["rowSet"] )

    #data["resultSets"][0]["rowSet"]
    for model in data["resultSets"][0]["rowSet"]:
        csvwriter.writerow(model)