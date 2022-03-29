import json

from GeoRun.models import Runner, Defi, Participation
from GeoRun.serializers import RunnerSerializer, DefiSerializer, ParticipationSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.views import APIView



class RunnerView(generics.ListCreateAPIView):
    serializer_class = RunnerSerializer

    @csrf_exempt
    def get_queryset(self):
        queryset = Runner.objects.all()
        mail = self.request.query_params.get('mail')
        pseudo = self.request.query_params.get('pseudo')
        password = self.request.query_params.get('password')
        if mail is not None:
            queryset = queryset.filter(mail=mail)
        if pseudo is not None:
            queryset = queryset.filter(pseudo=pseudo)
        if password is not None:
            queryset = queryset.filter(password=password)
        return queryset
    
    @csrf_exempt   
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = RunnerSerializer(data=data)
        if serializer.is_valid():
            quest = serializer.save()
            serializer = RunnerSerializer(quest)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class RunnerDetailView(APIView):
    model = Runner
    serializer_class = RunnerSerializer
    queryset = Runner.objects.all()

    def get_object(self, pk):
        try:
            return Runner.objects.get(pk=pk)
        except Runner.DoesNotExist:
            return HttpResponse(status=404)

    @csrf_exempt
    def get(self, request, pk, format=None):
        runner = self.get_object(pk)
        serializer = RunnerSerializer(runner)
        return JsonResponse(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        runner = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = RunnerSerializer(runner, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk=None):
        runner =self.get_object(pk)
        runner.delete()
        return HttpResponse(status=204)

class DefiView(generics.ListCreateAPIView):
    serializer_class = DefiSerializer

    @csrf_exempt
    def get_queryset(self):
        queryset = Defi.objects.all()
        nom = self.request.query_params.get('nom')
        date_creation = self.request.query_params.get('date_creation')
        if nom is not None:
            queryset = queryset.filter(nom=nom)
        if date_creation is not None:
            queryset = queryset.filter(date_creation=date_creation)
        return queryset
    
    @csrf_exempt   
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = DefiSerializer(data=data)
        if serializer.is_valid():
            quest = serializer.save()
            serializer = DefiSerializer(quest)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class DefiDetailView(APIView):
    model = Defi
    serializer_class = DefiSerializer
    queryset = Defi.objects.all()

    def get_object(self, pk):
        try:
            return Defi.objects.get(pk=pk)
        except Defi.DoesNotExist:
            return HttpResponse(status=404)

    @csrf_exempt
    def get(self, request, pk, format=None):
        defi = self.get_object(pk)
        serializer = DefiSerializer(defi)
        return JsonResponse(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        defi = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = DefiSerializer(defi, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk=None):
        defi =self.get_object(pk)
        defi.delete()
        return HttpResponse(status=204)

class ParticipationView(generics.ListCreateAPIView):
    serializer_class = ParticipationSerializer

    @csrf_exempt
    def get_queryset(self):
        queryset = Participation.objects.all()
        participant = self.request.query_params.get('participant')
        defi = self.request.query_params.get('defi')

        if participant is not None:
            queryset = queryset.filter(participant=participant)
        if defi is not None:
            queryset = queryset.filter(defi=defi)
        return queryset

    @csrf_exempt   
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ParticipationSerializer(data=data)
        if serializer.is_valid():
            quest = serializer.save()
            serializer = ParticipationSerializer(quest)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def get_result(request, name):
        resultats={}
        nomDefi=""
        queryset=Participation.objects.all()
        for participation in queryset:
            if participation.defi.nom == name:
                pseudo=participation.participant.pseudo
                resultats[pseudo]= participation.score
        return JsonResponse(resultats, status=201)

class ParticipationDetailView(APIView):
    model = Participation
    serializer_class = ParticipationSerializer
    queryset = Participation.objects.all()

    def get_object(self, pk):
        try:
            return Participation.objects.get(pk=pk)
        except Participation.DoesNotExist:
            return HttpResponse(status=404)

    @csrf_exempt
    def put(self, request, pk, format=None):
        participation = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = ParticipationSerializer(participation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk=None):
        participation=self.get_object(pk)
        participation.delete()
        return HttpResponse(status=204)
    

