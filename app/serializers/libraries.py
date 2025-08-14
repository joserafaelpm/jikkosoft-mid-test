from rest_framework import serializers
from ..models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
    
    def create(self, validated_data):
        name = validated_data['name']
        telephone = validated_data['telephone']
        if Library.objects.filter(name=name).exists():
            raise serializers.ValidationError("Existe una biblioteca con este nombre." \
            "Por favor, elige otro nombre.")
        if not isinstance(telephone, str):
            raise serializers.ValidationError("El número de teléfono debe ser un caracter.")
        
        return Library.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
    def __str__(self):
        return self.instance.name if self.instance else "Library Serializer"
        