from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer


def get_drinks(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks_data":serializer.data})