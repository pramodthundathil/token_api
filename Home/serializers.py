from rest_framework.serializers import ModelSerializer
from .models import PatientDetails, Tokens


class PatientDetailsSerializers(ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = "__all__"
        
class TokenSerializer(ModelSerializer):
    class Meta:
        model = Tokens
        fields  = "__all__"