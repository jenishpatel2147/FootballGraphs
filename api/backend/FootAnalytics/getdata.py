from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import mpld3
os.environ['KMP_DUPLICATE_LIB_OK']='True'

fbrefadderURL = 'http://fbref.com'

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
    df = df.groupby(df.country)  # Group Data by Country
    # Assign Each Country with specific Data
    italy,france,germany,spain,england = df.get_group('it'), df.get_group('fr'), df.get_group('de'), df.get_group('es'), df.get_group('eng') 
    return italy,france,germany,spain,england,df

def ScrapTeamPage(url, players):
    # Url - Team Url, 
    # players - True if you want total for all players 
    # players - False if you want simply opponent and squad total
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    table = soup.find("table", attrs={"class": "stats_table"})
    
    if players: 
        looper = table.tbody.find_all("tr")
        data = dict({"playerLink": [],
                    "playerName": []})
    else:
        looper = table.tfoot.find_all("tr")
        data = dict({"team_type": []})
        
    for tr in looper:
        if players:
            data.get("playerLink").append(tr.a.get("href"))
            data.get("playerName").append(tr.th.a.contents[0])
        else:
            data.get("team_type").append(str(tr.th.contents[0]))
            
        for td in tr.find_all("td"):
            col = td.get("data-stat").strip()
            if col not in data:
                data[col] = []
            
            if players:
                if col == "nationality":
                    data.get(col).append(td.span.contents[1].strip())
                elif col == "matches":
                    data.get(col).append("")
                elif len(td.contents) > 0:
                    if (col == "npxg_per90" or col == "xa_per90" or
                        col == "xg_per90"):
                        data.get(col).append(float(td.contents[0]))
                    else:
                        data.get(col).append(str(td.contents[0]))
                        
                else:
                    if td.contents == []:
                        data.get(col).append('0')
                    else:
                        data.get(col).append(str(td.contents[0]))
            else:
                if len(td.contents) > 0:
                    data.get(col).append(str(td.contents[0]))
                else:
                    data.get(col).append("")                
    df = pd.DataFrame(data)
    return df   


def per90sdiff(df, value): # 
    filtered_df = df.loc[df['minutes_90s'] >= str(value)] 
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


def generateviz():
    big5url = "https://fbref.com/en/comps/Big5/Big-5-European-Leagues-Stats"

    italy,france,germany,spain,england,ALL = ScrapBig5Page(big5url)
    players = pd.DataFrame()
    iters = 0 
    for index,row in england.iterrows():
        teamURL = row['squad'][2]
        temp = ScrapTeamPage(teamURL, True)
        players = pd.concat([temp,players], axis=0)
        iters +=1
        if iters % 5 == 0:
            print("Finished "+ str(iters) + " teams")

    per90sPlayers = per90sdiff(players, 5)
    players = getSpecificPositon(per90sPlayers, "att")

    fig, ax = plt.subplots()

    x = players['npxg_per90'].to_numpy()
    y = players['xa_per90'].to_numpy()
    names = players['playerName'].to_numpy()
    scatterplot = ax.scatter(x,y, color='b', alpha=0.6, edgecolor='black')
        
    ax.set_xlabel('NP Expected Goals', size=20)
    ax.set_ylabel('Expected Assists', size=20)
    ax.set_title('NP Expected Goals vs Expected Assists - data by FBref', size=20)

    #plt.xscale('log') -- Perhaps Nerd Mode
    #plt.yscale('log') -- Perhaps Nerd Mode

    plt.style.use('grayscale')  # to get seaborn scatter plot

    #paths = somelist of images...........

    #for x0, y0, path in zip(x, y, paths):
    #    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    #    ax.add_artist(ab)


    labels = ['{0}'.format(names[i]) for i in range(len(names))]
    tooltip = mpld3.plugins.PointLabelTooltip(scatterplot, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    mpld3.fig_to_html(fig)
