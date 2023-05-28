from django.forms import model_to_dict
from django.shortcuts import render
from djoser.serializers import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CarInfo
from .serializers import CarInfoSerializer


class CarInfoApiView(APIView):

    def get(self, request):
        cars = CarInfo.objects.filter(user_id=request.user.id)
        serializer = CarInfoSerializer(cars, many=True)
        return Response({'posts': serializer.data})

    def post(self, request):
        serializer = CarInfoSerializer(data=request.data)
        request.data["user"] = request.headers["Authorization"]
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response({'post': serializer.data, }, status=status.HTTP_201_CREATED)

    def put(self, request, pk, *args, **kwargs):

        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = CarInfo.objects.get(pk=pk)
        except:
            Response({"error": "Object does not exists"})

        serializer = CarInfoSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        if not user_id:
            return Response({'error': 'Method DELETE not allowed'})
        try:
            record = CarInfo.objects.filter(user_id= user_id)
            if not record:
                return Response({'error': "Object does not exist"})
            record.delete()
        except:
            return Response({'error': "Object does not exist"})

        return Response({"post": "delete info about car with user id: " + str(user_id)})


# class CarInfoApiView(generics.ListAPIView):
#     queryset = CarInfo.objects.all()
#     serializer_class = CarInfoSerializer
