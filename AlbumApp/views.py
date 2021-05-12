from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AlbumApp.models import Albums,Groups
from AlbumApp.serializers import AlbumSerializer,GroupSerializer

# GROUP API
@csrf_exempt
def groupApi(request,id=0):
    # GET REQUEST
    if request.method=='GET':
        groups = Groups.objects.all()
        groups_serializer = GroupSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)
    # POST REQUEST
    elif request.method=='POST':
        group_data = JSONParser().parse(request)
        group_serializer = GroupSerializer(data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse("Added Group Successfully", safe=False)
        return JsonResponse("Failed to Add Group", safe=False)
    # PUT REQUEST
    elif request.method=='PUT':
        group_data = JSONParser().parse(request)
        group = Groups.objects.get(GroupId=group_data['GroupId'])
        group_serializer = GroupSerializer(group,data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse("Updated Group Successfully", safe=False)
        return JsonResponse("Failed to Update Group", safe=False)

    elif request.method=='DELETE':
        group = Groups.objects.get(GroupId=id)
        group.delete()
        return JsonResponse("Deleted Group Successfully", safe=False)