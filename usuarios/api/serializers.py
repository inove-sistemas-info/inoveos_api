from rest_framework.serializers import ModelSerializer
from usuarios.models import Usuarios

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'