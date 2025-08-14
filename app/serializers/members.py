import re
from rest_framework import serializers
from ..models import Library, Member
    
class MemberSerializer(serializers.ModelSerializer):
    library = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all())
    
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        """
            Validate that the password is secure:
            - Minimum 8 characters
            - At least 1 uppercase letter
            - At least 1 lowercase letter
            - At least 1 number
        """
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
        return value

    def create(self, validated_data):
        member = Member(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            library=validated_data['library']
        )
        member.set_password(validated_data['password'])
        member.save()
        return member
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.library = validated_data.get('library', instance.library)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance