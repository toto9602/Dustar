from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChallengeSerializer
from .models import Challenge
from django.shortcuts import get_object_or_404

class ChallengeList(APIView):

    serializer_class = ChallengeSerializer

    def get(self, request):
        challenges = Challenge.objects.all()
        if challenges:
            serializer = ChallengeSerializer(challenges, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_204_NO_CONTENT)
        
        

    def post(self, request):
        serializer = ChallengeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ChallengeDetail(APIView):

    def get_object(self, pk):
        challenge = get_object_or_404(Challenge, pk=pk)
        return challenge

    def get(self, request, pk):
        challenge = self.get_object(pk=pk)
        serializer = ChallengeSerializer(challenge)
        return Response(serializer.data)

    def put(self, request, pk):
        challenge = self.get_object(pk=pk)
        serializer = ChallengeSerializer(challenge, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        challenge = self.get_object(pk=pk)
        challenge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

