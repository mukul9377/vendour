from django.shortcuts import render
from rest_framework import generics
from .serializers import VendingMachineSerializer
from .models import VendingMachine

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our rest api."""
    queryset = VendingMachine.objects.all()
    serializer_class = VendingMachineSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new vendingmachine"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETEE request"""

    queryset = VendingMachine.objects.all()
    serializer_class = VendingMachineSerializer
