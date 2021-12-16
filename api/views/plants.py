from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from ..serializers.plant import PlantSerializer
from ..models.plant import Plant
from django.core.exceptions import PermissionDenied

from api.models import plant 

class PlantsView(APIView):
    def post(self, request):
        # Add the user id as author
        request.data['author'] = request.user.id
        plant = PlantSerializer(data=request.data)
        if plant.is_valid():
            plant.save()
            return Response(plant.data, status=status.HTTP_201_CREATED)
        else:
            return Response(plant.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        # filter for mangos with our user id
        plants = Plant.objects.all()
        data = PlantSerializer(plants, many=True).data
        return Response(data)

class PlantView(APIView):
    def delete(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != plant.author:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk)
        data = PlantSerializer(plant).data
        return Response(data)
    
    def patch(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != plant.author:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Ensure the owner field is set to the current user's ID
        request.data['author'] = request.user.id
        updated_plant = PlantSerializer(plant, data=request.data)
        if updated_plant.is_valid():
            updated_plant.save()
            return Response(updated_plant.data)
        return Response(updated_plant.errors, status=status.HTTP_400_BAD_REQUEST)