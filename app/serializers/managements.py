from django.utils import timezone
from rest_framework import serializers
from ..models import Management, Member, Book
    
class ManagementSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Management
        fields = '__all__'

    def validate(self, data):
        member = data.get('member')
        book = data.get('book')
        if not Member.objects.filter(id=member.id).exists():
            raise serializers.ValidationError({"member": "El miembro especificado no existe."})
        if not Book.objects.filter(id=book.id).exists():
            raise serializers.ValidationError({"book": "El libro especificado no existe."})
        
        get_member = Member.objects.filter(id=member.id).first()
        get_book = Book.objects.filter(id=book.id).first()
        if get_member and get_book:
            if get_member.library != get_book.library:
                raise serializers.ValidationError({"library": "El miembro y el libro deben pertenecer a la misma biblioteca."})
            
        return data
    
    def create(self, validated_data):
        book = validated_data.get('book')
        member = validated_data.get('member')
        if Management.objects.filter(member=member, book=book, is_returned=False).exists():
            raise serializers.ValidationError({"member": "El miembro ya tiene este libro asignado y no lo ha devuelto."})
        elif Management.objects.filter(member=member, is_returned=False).first():
            raise serializers.ValidationError({"member": "El miembro ya tiene un libro asignado y no lo ha devuelto."})
        
        if book.items_available <= 0:
            raise serializers.ValidationError({"book": "No hay unidades disponibles de este libro."})
        book.items_available -= 1
        book.save()
        management = Management(
            member=validated_data['member'],
            book=validated_data['book'],
            is_returned=validated_data.get('is_returned', False)
        )
        management.save()
        return management

    def update(self, instance, validated_data):
        if instance.is_returned:
            raise serializers.ValidationError({"is_returned": "No se puede actualizar una gestión ya devuelta."})
        instance.member = validated_data.get('member', instance.member)
        instance.book = validated_data.get('book', instance.book)
        instance.is_returned = validated_data.get('is_returned', instance.is_returned)
        if  instance.is_returned and instance.returned_at is None:
            instance.returned_at = timezone.now()
            instance.book.items_available += 1
            instance.book.save()
        instance.save()
        return instance
    
    def delete(self, instance):
        if not instance.is_returned:
            instance.book.items_available += 1
            instance.book.save()
        instance.delete()
        return instance