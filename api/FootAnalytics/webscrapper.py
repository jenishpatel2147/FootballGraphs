from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json
os.environ['KMP_DUPLICATE_LIB_OK']='True'

fbrefadderURL = 'http://fbref.com'

'''
def try_and_except():
    try:

    except:

    return data
'''

def ScrapBig5Page(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    table = soup.find("table", attrs={"class": "stats_table"})
    data = dict({})
    for tr in table.tbody.find_all("tr"):
        if tr.get("class") != "thead":
            for td in tr.find_all("td"):
                col = td.get("data-stat").strip()
                if col not in data:
                    data[col] = []
        
                if col == "squad":
                    data.get(col).append([td.a.contents[0],
                                          td.img.get("src"), 
                                          str(fbrefadderURL + td.a.get("href"))])
                elif col == "country":
                    data.get(col).append(td.span.contents[0])
                elif (col == "top_team_scorers" or col == "top_keeper"):
                    data.get(col).append(td.a.contents[0])
                elif (col == "last_5"):
                    lst = []
                    for div in td.div.find_all("div"):
                        lst.append(div.a.contents[0])
                    data.get(col).append(lst)
                else:
                    data.get(col).append(td.contents[0])
   
    df = pd.DataFrame(data)      # Convert to DataFrame
    groupedCountries = df.groupby(df.country)  # Group Data by Country
    # Assign Each Country with specific Data
    italy,france,germany,spain,england = groupedCountries.get_group('it'), groupedCountries.get_group('fr'), groupedCountries.get_group('de'), groupedCountries.get_group('es'), groupedCountries.get_group('eng') 
    return italy,france,germany,spain,england,df

def ScrapTeamPage(url, players, country):
    # Url - Team Url, 
    # players - True if you want total for all players 
    # players - False if you want simply opponent and squad total
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    table = soup.find("table", attrs={"class": "stats_table"})

    numbers = ["games", "games_starts", "minutes", "minutes_90s", "goals", "assists", "goals_pens", "pens_made", "pens_att", 
        "cards_yellow", "cards_red", "goals_per90", "assists_per90", "goals_assists_per90", "goals_pens_per90", "goals_assists_pens_per90",
        "xg", "npxg", "xa", "npxg_xa", "xg_per90", "xa_per90", "xg_xa_per90", "npxg_per90", "npxg_xa_per90"]

    team_name = (url.split('-Stats')[0]).split('/')[-1]
    github_url =  "https://github.com/jenishpatel2147/FootballGraphs/blob/main/logos/" + country + "/" + team_name + ".png"

    if players: 
        looper = table.tbody.find_all("tr")
        data = dict({"playerLink": [],
                    "playerName": [],
                    "team": team_name,
                    "logo_url": github_url})
    else:
        looper = table.tfoot.find_all("tr")
        data = dict({"team_type": []})
        
    for tr in looper:
        if players:
            try:
                link = tr.a.get("href")
            except:
                link = "None"
            try:
                playerName = tr.th.a.contents[0]
            except:
                playerName = "None"

            data.get("playerLink").append(link)
            data.get("playerName").append(playerName)

        else:
            data.get("team_type").append(str(tr.th.contents[0]))
            
        for td in tr.find_all("td"):
            col = td.get("data-stat").strip()
            if col not in data:
                data[col] = []
            
            if players:
                if col == "nationality":
                    try:
                        nationality = td.span.contents[1].strip()
                    except:
                        nationality = "Could Not Find Nationality"
                    data.get(col).append(nationality)
                elif col == "matches":
                    data.get(col).append("")
                elif len(td.contents) > 0:
                    if (col in numbers):
                        data.get(col).append(float(td.contents[0].replace(',','')))
                    else:
                        data.get(col).append(str(td.contents[0]))
                        
                else:
                    if td.contents == []:
                        data.get(col).append(0)
                    else:
                        data.get(col).append(str(td.contents[0]))
            else:
                if len(td.contents) > 0:
                    data.get(col).append(str(td.contents[0]))
                else:
                    data.get(col).append("")                
    df = pd.DataFrame(data)
    return df   


def per90sdiff(df, value=5): # 
    filtered_df = df.loc[df['minutes_90s'] >= float(value)] 
    return filtered_df
    

def getSpecificPositon(df, pos): #FW,AM,RW,LW
    # pos = "att", "mid", "full", "def", "wing"
    if pos == "att":
        values=['FW','AM','RW','LW']
    elif pos == "mid":
        values=['WM','RM','LM','CM','DM', 'MF']
    elif pos == "full":
        values=['FB','RB','LB']
    elif pos == "def":
        values=['CB']    
    else : # pos == "wing"
        values=['LW','RW']
    
    filtered_df = df.loc[df['position'].isin(values)]
    return filtered_df


def getdata():
    big5url = "https://fbref.com/en/comps/Big5/Big-5-European-Leagues-Stats"

    italy,france,germany,spain,england,ALL = ScrapBig5Page(big5url)

    countries = [italy, france, spain, england, germany]
    fileNames = ["italy", "france", "spain", "england", "germany"]

    for i in range(0, len(countries)):
        print("Starting - " + str(fileNames[i]))
        players = pd.DataFrame()
        iters = 0 
        league = countries[i]
        name = fileNames[i]
        
        for index,row in league.iterrows():
            teamURL = row['squad'][2]
            temp = ScrapTeamPage(teamURL, True, name)
            players = pd.concat([temp,players], axis=0)
            iters +=1
            if iters % 5 == 0:
                print("Finished "+ str(iters) + " teams")

        d = [ 
            dict([
                (colname, row[i])
                for i,colname in enumerate(players.columns)
            ])
            for row in players.values
        ]

        jsonData = json.dumps(d, indent=4)

        fileName = './' + name + '_players.json'
        with open(fileName, 'w') as outputFile:
            print(jsonData, file=outputFile)
        
        print("Finished - " + str(fileNames[i]))