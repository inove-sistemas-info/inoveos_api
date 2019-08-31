from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuarios
from .serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer