from json.encoder import JSONEncoder
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import *
from django.core import serializers
import json

# Create your views here.
def index(request):
     context = RequestContext(request, {
        'servers': Server.objects.all(),
     })
     return render_to_response("monitor/index.html",{},context)

def loadData(request):

    servers = Server.objects.all();
    dataToRender = []

    for index in range(len(servers)):
        serverData = {}
        serverData['elementName'] = servers[index].alias
        serverData['data'] = getServerData(servers[index]);
        dataToRender.append(serverData)

    jsonData = json.dumps(dataToRender,cls=PythonObjectEncoder)

    return HttpResponse(jsonData)

def getServerData(server):
    arr = []
    for stat in Stat.objects.filter(server=server).order_by('time'):
      arr.append(stat)
    return  arr


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'time': obj.time.strftime("%I:%M%p"), 'network_speed' : obj.network_speed, 'cpu_load': obj.cpu_load , 'cpu_usage': obj.cpu_usage, 'free_ram': obj.free_ram }