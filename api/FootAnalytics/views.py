# import Http Response from django
from datetime import time
from django.http import HttpResponse
import requests
from .getdata import generateviz, rendernewdata
import multiprocessing as mp
import time


def refresh(request):
    response = rendernewdata()
    return HttpResponse(response)


# Create your views here.
def footy(request):
    try:
        league =  request.GET['league']
        per90s = request.GET['per90s']
        position = request.GET['position']
        xlabel = request.GET['xlabel']
        ylabel = request.GET['ylabel']
        title = request.GET['title']
        read_new = request.GET['read_new']
        x_metric = request.GET['x_metric']
        y_metric = request.GET['y_metric']
        display_names = request.GET['display_names']
        #color = request.GET['color']

    except:
        league = "england"
        per90s = 5
        position = "att"
        xlabel = "NP Expected Goals"
        ylabel = "Expected Assists"
        title = "Contact Creator Wierd Stuff Happening"
        read_new = True
        x_metric = "goals_per90"
        y_metric = "assists_per90"
        display_names = False
        #color = '#c2c1c0'

    if display_names == "true":
        display_names = True
    else:
        display_names = False
    
    viz = generateviz(league, per90s, position, xlabel, ylabel, title, read_new, x_metric, y_metric, display_names)
    return HttpResponse(viz)
