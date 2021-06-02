from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **Kwargs):
    return Response(data="Only for logged in users", status=status.HTTP_200_OK)
