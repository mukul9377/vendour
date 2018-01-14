from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variable"""
        self.client = APIClient()
        self.vendingmachine_data = {'machineCode': 'M001'}
        self.response = self.client.post(
            reverse('create'),
            self.vendingmachine_data,
            format="json")


    """def test_model_can_create_a_machine(self):
        #Test the Vending Machine model can create a list of racks
        old_count = VendingMachine.objects.count()
        self.vendingMachine.save()
        new_count = VendingMachine.objects.count()
        self.assertNotEqual(old_count, new_count)"""

    def test_api_can_create_a_vendingmachine(self):
        """Test the api has vending machine creation capability"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    
