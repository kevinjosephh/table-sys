from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime,timedelta,time,timezone

from . serializers import *
from . models import *
# Create your views here.

@api_view(('GET',))
def table(request):
    table=Table.objects.all()
    serializer=TableSerializer(table,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def booktable(request,id):
    table=Table.objects.get(id=id)
    if table:
        if table.status == "Empty":
            endtime = time(23, 00, 00, 000000)
            starttime= time(1, 00, 00, 000000)
            t=datetime.now().time()
            if endtime >= t >= starttime:
                if (datetime.now() >= table.time + timedelta(minutes=10)):
                    table.status = "Occupied"
                    table.time = datetime.now()
                    table.save()
                    data = "Booked"
                    return Response(data)
                else:
                    data=f"This table is being cleaned, try another table or wait for {table.time+timedelta(minutes=10) - datetime.now() }"
                    return Response(data)
            else:
                data= f"You can only book between 5pm to 11pm.current time is {t}"
                return Response(data)
        else:
            data = "Table is Occupied"
            return Response(data)
    else:
        data = "Table Does not exsists"
        return Response(data)

@api_view(['POST'])
def cleartable(request,id):
    table=Table.objects.get(id=id)
    if table:
        if table.status == "Occupied":
            table.status = "Empty"
            table.time = datetime.now()
            table.save()
            data = "Table Cleared"
            return Response(data)
        else:
            data="It is already empty"
            return Response(data)
    else:
        data = "Table Does not exsists"
        return Response(data)