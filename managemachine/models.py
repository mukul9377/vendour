from django.db import models

class VendingMachine(models.Model):
    """This class represents the vending machine model."""
    machineCode = models.CharField(max_length=255, blank=False, primary_key=True)
    activate_flag = models.BooleanField(default=True)
    """This field defines the the 2d matrix in form of JSON string"""
    definition = models.TextField('Vending Machine Racks definition in JSON')

    def __str__(self):
        return "{}".format(self.name)
