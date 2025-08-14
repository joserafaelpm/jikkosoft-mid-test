from rest_framework import serializers
from ..models import Library, Book

class BookSerializer(serializers.ModelSerializer):
    library = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all())

    class Meta:
        model = Book
        fields = '__all__'
    
    def create(self, validated_data):
        items_available = validated_data.get('items_available', 0)
        if items_available < 0:
            raise serializers.ValidationError("La cantidad de items disponibles no puede ser negativa.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        items_available = validated_data.get('items_available', instance.items_available)
        if items_available < 0:
            raise serializers.ValidationError("La cantidad de items disponibles no puede ser negativa.")
        return super().update(instance, validated_data)