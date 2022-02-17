from types import MemberDescriptorType
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
from pandas.core import api
import numpy as np
import os
import mpld3
import mplcursors
import io
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


def readData(country):
    fileName = './' + country + '_allplayers.json'
    with open(fileName, 'r') as myfile:
        data=myfile.read()

    # parse file
    obj=json.loads(data)

    # convert to DataFrame
    df=pd.DataFrame.from_dict(obj,orient='columns')

    return df


def getImage(team, country):
    try:
        path = './logos/' + country + '/' + team.replace('-', ' ') + '.png'
        data = OffsetImage(plt.imread(path), zoom=.09, alpha=1)
    except:
        path = './logos/' + country + '/' + team.replace('-', ' ') + '.png'
        print(path)
        path = './logos/england/Everton.png'
        data = OffsetImage(plt.imread(path), zoom=.09, alpha=1)

    return data


def generateviz(country, per90s, position, xlabel, ylabel, title, read_new, x_metric, y_metric, display_logos, get_icons=False):
    # print(read_new)
    # implement read_new correctly
    read_new = True
    if read_new:
        players = readData(country)
    else:
        players = last_read_players

    per90sPlayers = per90sdiff(players, per90s)
    players = getSpecificPositon(per90sPlayers, position)


    plt.figure(facecolor='yellow')
    plt.figure(linewidth=5)

    fig, ax = plt.subplots()

    # Before
    # xbefore = players[x_metric].to_numpy()
    # ybefore = players[y_metric].to_numpy()

    # Extract X and Y columns from data and converting it to a list in numpy
    x = players[x_metric].to_numpy()
    x = [d.get('value') for d in x]
    x = np.array(x)

    y = players[y_metric].to_numpy()
    y = [d.get('value') for d in y]
    y  = np.array(y)

    names = players['playerName'].to_numpy()

    # Used to Get Logo Path
    teams = players['team'].to_numpy()
         
    labelcolor = "#ff8080"
    facecolor  = "#121212"
    pointcolor = "#ff8080"

    # OLD
    # scatterplot = ax.scatter(x,y, color=pointcolor, alpha=0.8)

    if display_logos is True:
        alpha = 0
    else:
        alpha = 0.7

    scatter = ax.scatter(x,y, color=pointcolor, alpha=alpha)

    ax.set_facecolor(facecolor) 

    if display_logos is True:
        for x0, y0, team in zip(x, y, teams):
            ab = AnnotationBbox(getImage(team, country), (x0, y0), frameon=False)
            ax.add_artist(ab)

    ax.spines['bottom'].set_color('#dddddd')
    ax.spines['left'].set_color('#dddddd')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(axis='x', colors='green')
    ax.tick_params(axis='y', colors='green')



    # CHANGE THIS IS get_icons is True afterwards
   
    if False:
        for i, txt in enumerate(names):
            ax.annotate(txt, (x[i], y[i]), color="white", xy=(0,0), xytext=(20,20), arrowprops=dict(arrowstyle="->"))
    

    mplcursors.cursor(scatter, hover=True)

    """
    Temporay Hold due to 

    labels = ['{0}'.format(names[i]) for i in range(len(names))]
    tooltip = mpld3.plugins.PointHTMLTooltip(scatterplot, labels=labels, css=css)
    mpld3.plugins.connect(fig, tooltip)
    
    if False == True:
        # Removing All Interactivity from the graph
        mpld3.plugins.clear(fig)  # clear all plugins from the figure
    
    jsonfiles = mpld3.fig_to_html(fig)
    """ 

    print("Graph Created Successfull")

    imgdata = io.StringIO()

    # Setting Figure Size 
    size = "else"

    # Change Axis numbers size 
    # Change Alpha/Point size 

    if size == "small":
        set_size = (5,2)
        set_axis = 5
        set_pad = 7
        set_title = 7
    elif size == "semi-medium":
        set_size = (7,3)
        set_axis = 5
        set_pad = 10
        set_title = 7
    elif size == "medium":
        set_size = (9,4)
        set_axis = 5
        set_pad = 10
        set_title = 7
    else:   # large
        set_size = (14,6)
        set_axis = 14
        set_pad = 10
        set_title = 20

    ax.set_xlabel(xlabel, size=set_axis, color=labelcolor, labelpad=set_pad)
    ax.set_ylabel(ylabel, size=set_axis, color=labelcolor, labelpad=set_pad)
    ax.set_title(title, size=set_title, color=labelcolor, pad=set_pad, loc='left')
    plt.gcf().set_size_inches(set_size)

    plt.savefig(imgdata, dpi=1600, format='svg', transparent=True)

    f = open("figure.svg", "a")
    f.write(imgdata.getvalue())
    f.close()
    
    # Figure Out a way to not load and reload a svg file, would save time conseumption and logistics

    # last_read_players = players
    
    return imgdata.getvalue()
