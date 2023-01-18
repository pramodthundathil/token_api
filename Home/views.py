from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PatientDetailsSerializers, TokenSerializer
from .models import Tokens, PatientDetails



@api_view(["POST"])
def TokenGenerator(request):
    serializer = PatientDetailsSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        patient = PatientDetails.objects.all().last()
        try:
            Token = Tokens.objects.all().last()
            token = str(int(Token.Token)+1)
        except:
            token = "1"
            
        print(patient)
        T = Tokens.objects.create(Token = token, Patient = patient)
        T.save()
        tokenserilizer  = TokenSerializer(T,many = False)
        d = [serializer.data,tokenserilizer.data]
        return Response(d)
    
@api_view(["GET"])   
def AllPatientView(request):
    patients = PatientDetails.objects.all()
    tokens = Tokens.objects.all()
    DATA = [(PatientDetailsSerializers(patients,many = True)).data,(TokenSerializer(tokens,many= True)).data]
    return Response(DATA)
    

@api_view(["POST"])   
def DataTest(requst):
    d = [{"Patient_Name":"Pramod","Patient_Phone":"9141109785","Chair_Number":"4","Treatment_Category":"palluvedhana"}]
    return Response(d)