# import Http Response from django
from datetime import time
from django.http import HttpResponse
from .getdata import generateviz
import multiprocessing as mp
import time


# Create your views here.
def footy(request):
    try:
        league =  request.GET['league']
        per90s = request.GET['per90s']
    except:
        league = "england"
        per90s = 5
    viz = generateviz(league, per90s)
    return HttpResponse(viz)

# Create your views here.
