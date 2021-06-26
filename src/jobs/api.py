from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import JobSerializer
from .models import Job

@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()
    data = JobSerializer(jobs,many=True).data

    context = {
        'data' : data
    }
    return Response(context)


@api_view(['GET'])
def job_detail_api(request,id):
    job = Job.objects.get(id=id)
    data = JobSerializer(job).data

    context = {
        'data' : data
    }
    return Response(context)


class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
