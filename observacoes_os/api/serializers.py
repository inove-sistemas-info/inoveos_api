from rest_framework.serializers import ModelSerializer
from observacoes_os.models import ObservacoesOs

class ObservacaoOsSerializer(ModelSerializer):
    class Meta:
        model = ObservacoesOs
        fields = '__all__'