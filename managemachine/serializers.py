from rest_framework import serializers
from .models import VendingMachine

class VendingMachineSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = VendingMachine
        fields = ('machineCode', 'activate_flag', 'definition')
