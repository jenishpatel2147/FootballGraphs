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
from .webscrapper import extractdata
os.environ['KMP_DUPLICATE_LIB_OK']='True'

css = """
table
{
  border-collapse: collapse;
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
    extractdata()
    return "NEW DATA UPLODATED -- CHECK LOGS TO CONFIRM"

def per90sdiff(df, value=5): # 
    filtered_df = df.loc[df['minutes_90s'] >= float(value)] 
    return filtered_df
    

def getSpecificPositon(df, pos): #FW,AM,RW,LW
    # pos = "att", "mid", "full", "def", "wing", "all"
    if pos == "att":
        values=['FW','AM','RW','LW']
    elif pos == "mid":
        values=['WM','RM','LM','CM','DM', 'MF']
    elif pos == "full":
        values=['FB','RB','LB', 'DF']
    elif pos == "def":
        values=['CB','DM','LB','RB']    
    else: # pos == "all"
        values=['FW','AM','RW','LW','WM','RM','LM','CM','DM','MF','FB','RB','LB','CB','LW','RW']

    filtered_df = df.loc[df['position'].isin(values)]
    return filtered_df


def readData(team):
    fileName = './' + team + '_allplayers.json'
    with open(fileName, 'r') as myfile:
        data=myfile.read()

    # parse file
    obj=json.loads(data)

    # convert to DataFrame
    df=pd.DataFrame.from_dict(obj,orient='columns')

    return df


def getImage(path):
    print(path)
    return OffsetImage(plt.imread(path), zoom=.05, alpha=1)

def generateviz(team, per90s, position, xlabel, ylabel, title, read_new, x_metric, y_metric, display_names, get_icons=False):
    # print(read_new)
    # implement read_new correctly
    print(display_names)
    read_new = True
    if read_new:
        players = readData(team)
    else:
        players = last_read_players

    per90sPlayers = per90sdiff(players, per90s)
    players = getSpecificPositon(per90sPlayers, position)

    plt.figure(linewidth=5)

    fig, ax = plt.subplots()

    # Before
    xbefore = players[x_metric].to_numpy()
    ybefore = players[y_metric].to_numpy()
    #print(xbefore)

    # Extract X and Y columns from data and converting it to a list in numpy
    x = players[x_metric].to_numpy()
    x = [d.get('value') for d in x]
    x = np.array(x)

    y = players[y_metric].to_numpy()
    y = [d.get('value') for d in y]
    y  = np.array(y)

    names = players['playerName'].to_numpy()

    # paths = players['logo_url'].to_numpy()               # Change it to logo URL in the future

    path = '../../logos/england/Arsenal.png'
    
    labelcolor = "#ff8080"
    facecolor  = "#121212"
    pointcolor = "#ff8080"

    scatterplot = ax.scatter(x,y, color=pointcolor, alpha=0.8)

    ax.set_facecolor(facecolor) 
    ax.set_xlabel(xlabel, size=22, color=labelcolor)
    ax.set_ylabel(ylabel, size=22, color=labelcolor)
    ax.set_title(title, size=25, color=labelcolor)


    if get_icons is True:
        for x0, y0, path in zip(x, y, paths):
            ab = AnnotationBbox(OffsetImage(plt.imread(path)), (x0, y0), frameon=False)
            print(ab)
            ax.add_artist(ab)
   
    if display_names is True:
        for i, txt in enumerate(names):
            ax.annotate(txt, (x[i], y[i]))
    
    labels = ['{0}'.format(names[i]) for i in range(len(names))]
    tooltip = mpld3.plugins.PointHTMLTooltip(scatterplot, labels=labels, css=css)
    mpld3.plugins.connect(fig, tooltip)

    #jsonfiles = json.dumps(mpld3.fig_to_dict(fig))

    if False == True:
        # Removing All Interactivity from the graph
        mpld3.plugins.clear(fig)  # clear all plugins from the figure
    
    jsonfiles = mpld3.fig_to_html(fig)

    last_read_players = players
    print

    return jsonfiles
