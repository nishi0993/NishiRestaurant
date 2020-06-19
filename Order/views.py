from django.shortcuts import render
from django.http import HttpResponse
from Order.models import Restaurant, Place, Staff
from Order.serializers import StaffSerializer
import json
from pprint import pprint


def Homepage(request):
    staff1 = Staff.objects.all()
    staffs = StaffSerializer(staff1, many=True)
    print(type(staffs.data))
    response = json.dumps(staffs.data)
    pprint(response)
    #return render(request,'demo.html',{'staff1':staff1})
    return HttpResponse(response, content_type='application/json')
# Create your views here.
