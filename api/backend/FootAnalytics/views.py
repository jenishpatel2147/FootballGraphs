# import Http Response from django
from django.http import HttpResponse
from .getdata import generateviz
import multiprocessing as mp


# Create your views here.
def footy(request):
    viz = mp.Process(target=generateviz(), args=())
    viz.start()
    print(viz)
    return HttpResponse(viz)

# Create your views here.
