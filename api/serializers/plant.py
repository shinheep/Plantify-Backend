from rest_framework import serializers
from ..models.plant import Plant

class PlantSerializer(serializers.ModelSerializer):
    #Define meta class
    class Meta:
        #specify the model from which to define the fields
        model = Plant
        # Define fields to be returned
        fields = '__all__'