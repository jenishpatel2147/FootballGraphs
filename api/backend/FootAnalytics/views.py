# import Http Response from django
from datetime import time
from django.http import HttpResponse
import requests
from .getdata import generateviz
import multiprocessing as mp
import time


# Create your views here.
def footy(request):
    try:
        league =  request.GET['league']
        per90s = request.GET['per90s']
        xlabel = request.GET['xlabel']
        ylabel = request.GET['ylabel']
        title = request.GET['title']
        read_new = request.GET['read_new']
        x_metric = request.GET['x_metric']
        y_metric = request.GET['y_metric']
        #color = request.GET['color']

    except:
        league = "england"
        per90s = 5
        xlabel = "NP Expected Goals"
        ylabel = "Expected Assists"
        title = "NP Expected Goals vs Expected Assists - data by FBref"
        read_new = True
        x_metric = "npxg"
        y_metric = "xa_per90"
        #color = '#c2c1c0'

    position = "att"
    
    viz = generateviz(league, per90s, position, xlabel, ylabel, title, read_new, x_metric, y_metric)
    return HttpResponse(viz)

# Create your views here.
