from res_framework.serializers import ModelsSerialzer
from usuarios.models import Usuarios

class UsuarioSerializer(ModelsSerialzer):
    class Meta:
        model = Usuarios
        fields = '__all__'