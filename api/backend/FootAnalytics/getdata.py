import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
import numpy as np
import os
import mpld3
import json
from webscrapper import getdata
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def rendernewdata():
    getdata()
    return "NEW DATA UPLODATED -- CHECK LOGS TO CONFIRM"

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


def readData(team):
    fileName = './' + team + '_players.json'
    with open(fileName, 'r') as myfile:
        data=myfile.read()

    # parse file
    obj=json.loads(data)

    # convert to DataFrame
    df=pd.DataFrame.from_dict(obj,orient='columns')

    return df

def getImage(path):
    return OffsetImage(plt.imread(path), zoom=.05, alpha = 1)


def generateviz(team="england", per = 5, position = "att", color= "#c2c1c0"):
    getdata()
    players = readData(team)
    #print(players)

    per90sPlayers = per90sdiff(players, per)
    players = getSpecificPositon(per90sPlayers, position)

    fig, ax = plt.subplots()

    x = players['npxg_per90'].to_numpy()
    y = players['xa_per90'].to_numpy()
    names = players['playerName'].to_numpy()
    paths = players['path'].to_numpy()
    scatterplot = ax.scatter(x,y, color='b', alpha=0.6, edgecolor='black')
        
    ax.set_xlabel('NP Expected Goals', size=20)
    ax.set_ylabel('Expected Assists', size=20)
    ax.set_title('NP Expected Goals vs Expected Assists - data by FBref', size=20)

    plt.style.use('grayscale')  # to get seaborn scatter plot

    for x0, y0, path in zip(x, y, paths):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        ax.add_artist(ab)


    labels = ['{0}'.format(names[i]) for i in range(len(names))]
    tooltip = mpld3.plugins.PointLabelTooltip(scatterplot, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    #jsonfiles = json.dumps(mpld3.fig_to_dict(fig))
    jsonfiles = mpld3.fig_to_html(fig)

    return jsonfiles
