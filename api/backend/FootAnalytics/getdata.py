import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
import numpy as np
import os
import mpld3
import PIL
import requests
from io import BytesIO
import json
from .webscrapper import getdata
os.environ['KMP_DUPLICATE_LIB_OK']='True'

css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

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
    path = "https://raw.githubusercontent.com/jenishpatel2147/FootballGraphs/master/logos/england/Chelsea.png"
    response = requests.get(path)
    try:
        img = PIL.Image.open(BytesIO(response.content))
    except:
        img = PIL.Image.open(BytesIO(response.content))

    img = "https://raw.githubusercontent.com/jenishpatel2147/FootballGraphs/master/logos/england/Chelsea.png"
    return OffsetImage(img, zoom=.05, alpha=1)

LAST_READ_FILE = ''

def generateviz(team, per90s, position, xlabel, ylabel, title, read_new, x_metric, y_metric):
    
    if read_new:
        players = readData(team)
    else:
        players = LAST_READ_FILE

    per90sPlayers = per90sdiff(players, per90s)
    players = getSpecificPositon(per90sPlayers, position)

    fig, ax = plt.subplots()

    x = players[x_metric].to_numpy()
    y = players[y_metric].to_numpy()
    names = players['playerName'].to_numpy()
    # paths = players['url'].to_numpy()               # Change it to logo URL in the future
    
    scatterplot = ax.scatter(x,y, color='green', alpha=0.7)

    # for x0, y0, path in zip(x, y, paths):
    #    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    #    ax.add_artist(ab)

    ax.set_facecolor('#121212') 

    color = "#ff8080"
    ax.set_xlabel(xlabel, size=22, color=color)
    ax.set_ylabel(ylabel, size=22, color=color)
    ax.set_title(title, size=25, color=color)

    #plt.style.use('grayscale')  # to get seaborn scatter plot

    labels = ['{0}'.format(names[i]) for i in range(len(names))]
    tooltip = mpld3.plugins.PointHTMLTooltip(scatterplot, labels=labels, css=css)
    mpld3.plugins.connect(fig, tooltip)

    #jsonfiles = json.dumps(mpld3.fig_to_dict(fig))
    jsonfiles = mpld3.fig_to_html(fig)


    LAST_READ_FILE = players

    return jsonfiles
