from rest_framework import serializers
from .models import ElectronicsNetwork, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ElectronicsNetworkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)  # 🔒 Запрет на изменение
    supplier = serializers.StringRelatedField(read_only=True)  # Только для чтения в API

    class Meta:
        model = ElectronicsNetwork
        fields = '__all__'

    def validate(self, data):
        """
        Уровень должен определяться автоматически.
        Поля debt и supplier нельзя менять через API.
        """
        if 'level' in self.initial_data:
            raise serializers.ValidationError("Уровень определяется автоматически через поставщика.")
        return data