from django.shortcuts import render 
from rest_framework import status
from Spec.serializers import InfoCompanySerializer, SeguridadSocialSerializer
from Spec.models import InfoCompany, SeguridadSocial
from rest_framework.decorators import api_view
from rest_framework.response import Response 



@api_view(['GET']) 
def info_company_list(request):
    if request.method == 'GET':
        companys = InfoCompany.objects.all()
        company_serializer = InfoCompanySerializer(companys, many=True)
        return Response(company_serializer.data)

@api_view(['GET']) 
def info_company_detail(request, pk):
    try:
        company = InfoCompany.objects.get(pk=pk)
    except InfoCompany.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        company_serializer = InfoCompanySerializer(company) 
        return Response(company_serializer.data)



@api_view(['GET']) 
def seguridad_social_detail(request, pk):
    try:
        empresa = SeguridadSocial.objects.get(pk=pk)
    except SeguridadSocial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        seg_soci_serializer = SeguridadSocialSerializer(empresa)
        return Response(seg_soci_serializer.data)