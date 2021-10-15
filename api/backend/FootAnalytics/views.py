# import Http Response from django
from datetime import time
from django.http import HttpResponse
from .getdata import generateviz
import multiprocessing as mp
import time


# Create your views here.
def footy(request):
    print(request)

    viz = generateviz()
    return HttpResponse(viz)

# Create your views here.
