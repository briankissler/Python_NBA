import json
import requests
import traceback
import csv

def searchApi(query):
    print("starting...")
    endpoint = "https://stats.nba.com/stats/playergamelogs"
    data = {
            "DateFrom":"",
            "DateTo":"",
            "GameSegment":"",
            "LastNGames":query,
            "LeagueID":"00",
            "Location":"",
            "MeasureType":"Base",
            "Month":"0",
            "OpponentTeamID":"0",
            "Outcome":"",
            "PORound":"0",
            "PaceAdjust":"N",
            "PerMode":"Totals",
            "Period":"0",
            "PlusMinus":"N",
            "Rank":"N",
            "Season":"2021-22",
            "SeasonSegment":"",
            "SeasonType":"Regular Season",
            "ShotClockRange":"",
            "VsConference":"",
            "VsDivision":""
    }

    headers = { "Accept": "application/json, text/plain, */*",
                "Origin": "https://www.nba.com",
                "Accept-Encoding": "gzip, deflate, br",
                "Host": "stats.nba.com",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
                "Referer": "https://www.nba.com/",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "x-nba-stats-origin": "stats",
                "x-nba-stats-token": "true"
            } 
    try:
        print("getting..")
        #response = requests.get(endpoint, data=data, headers = {"Accept": "application/json, text/plain, */*"} )
        r = requests.get(endpoint, params = data, headers = headers )
        print(r.request.headers)
        print(r.request.url)
        print(r.request.body)
        response = r
        if(response.status_code == 200):

            data = response.json()

            print( data["parameters"] )

            #print(data["resultSets"][0]["headers"])
            #for msg in response:
                #print(msg)
                #print(response.json() )
                #response = response.json()
            
            with open('NBA_Last10.csv', 'w', newline='', encoding='utf-8') as pt_data1:
                csvwriter = csv.writer(pt_data1)
                csvwriter.writerow( data["resultSets"][0]["headers"] )
                for model in data["resultSets"][0]["rowSet"]:
                    csvwriter.writerow(model)
    except Exception:
        print(traceback.format_exc())


searchApi("10")        