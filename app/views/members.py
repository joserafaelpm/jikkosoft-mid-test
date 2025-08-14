from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import ProtectedError
from ..models import Member, Management
from ..serializers import MemberSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#----------------------------------------------------------------
# CRUD for Member
#----------------------------------------------------------------
@swagger_auto_schema(
    method='get',
    operation_summary="Obtener lista de miembros",
    operation_description="Lista todos los miembros",
    responses={200: openapi.Response('Lista de miembros', MemberSerializer(many=True))},
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def member_list(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    res = {
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='get',
    operation_summary="Obtener un miembro por su ID",
    operation_description="Obtiene un miembro por su ID",
    responses={200: openapi.Response('Miembro encontrado', MemberSerializer)}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def member_detail(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        res = {
            'msg': 'El miembro con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = MemberSerializer(member)
    res = {
        'msg': 'Miembro encontrado',
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='post',
    operation_summary="Crea un nuevo miembro",
    operation_description="Crea un nuevo miembro",
    request_body=MemberSerializer,
    responses={201: openapi.Response('Miembro creado correctamente', MemberSerializer)}
)
@api_view(['POST'])
def member_create(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Miembro creado correctamente',
            'status': 200,
            'data': serializer.data
        }
        return Response(res, status=200)
    res = {
        'msg': 'Error al crear el miembro',
        'status': 540,
        'data': serializer.errors
    }
    return Response(res, status=540)

@swagger_auto_schema(
    method='put',
    operation_summary="Actualiza un miembro existente por ID",
    operation_description="Actualiza un miembro existente por ID",
    request_body=MemberSerializer,
    responses={200: openapi.Response('Miembro actualizado correctamente', MemberSerializer)}
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def member_update(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        res = {
            'msg': 'El miembro con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = MemberSerializer(member, data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Miembro actualizado correctamente',
            'status': 200,
            'data': serializer.data
        }
        return Response(res, status=200)
    res = {
        'msg': 'Error al actualizar el miembro',
        'status': 540,
        'data': serializer.errors
    }
    return Response(res, status=540)

@swagger_auto_schema(
    method='delete',
    operation_summary="Elimina un miembro existente por ID",
    operation_description="Elimina un miembro existente por ID",
    responses={200: 'Miembro eliminado correctamente', 404: 'Miembro no encontrado', 409: 'Conflicto al eliminar el miembro'}
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def member_delete(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        res = {
            'msg': 'El miembro con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    try:
        member.delete()
        res = {
            'msg': 'Miembro eliminado correctamente',
            'status': 200
        }
        return Response(res, status=200)
    except ProtectedError as e:
        management_count = Management.objects.filter(member_id=pk).count()
        res = {
            'msg': f'No se puede eliminar el miembro porque está asociado a {management_count} gestión(es).',
            'status': 409
        }
        return Response(res, status=409)