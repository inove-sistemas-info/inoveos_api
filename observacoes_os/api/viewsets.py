from rest_framework.viewsets import ModelViewSet
from observacoes_os.models import ObservacoesOs
from .serializers import ObservacaoOsSerializer

class ObservacaoOsViewSet(ModelViewSet):
    queryset = ObservacoesOs.objects.all()
    serializer_class = ObservacaoOsSerializer 