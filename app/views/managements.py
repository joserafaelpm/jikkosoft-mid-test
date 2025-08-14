from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import Management
from ..serializers import ManagementSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#----------------------------------------------------------------
# CRUD for Management
#----------------------------------------------------------------
@swagger_auto_schema(
    method='get',
    operation_summary="Lista todas las gestiones",
    operation_description="Lista todas las gestiones",
    responses={200: openapi.Response('Lista de gestiones', ManagementSerializer(many=True))}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def management_list(request):
    managements = Management.objects.all()
    serializer = ManagementSerializer(managements, many=True)
    res = {
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='get',
    operation_summary="Obtiene una gestion por su ID",
    operation_description="Obtiene una gestion por su ID",
    responses={200: openapi.Response('Gestion encontrada', ManagementSerializer)}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def management_detail(request, pk):
    try:
        management = Management.objects.get(pk=pk)
    except Management.DoesNotExist:
        res = {
            'msg': 'La gestion con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = ManagementSerializer(management)
    res = {
        'msg': 'Gestion encontrada',
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='post',
    operation_summary="Crea una nueva gestion",
    operation_description="Crea una nueva gestion",
    request_body=ManagementSerializer,
    responses={201: openapi.Response('Gestion creada correctamente', ManagementSerializer)}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def management_create(request):
    serializer = ManagementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Gestion creada correctamente',
            'status': 200,
            'data': serializer.data
        }
        return Response(res, status=200)
    res = {
        'msg': 'Error al crear la gestion',
        'status': 540,
        'data': serializer.errors
    }
    return Response(serializer.errors, status=540)

@swagger_auto_schema(
    method='put',
    operation_summary="Actualiza una gestion existente por ID",
    operation_description="Actualiza una gestion existente por ID",
    request_body=ManagementSerializer,
    responses={200: openapi.Response('Gestion actualizada correctamente', ManagementSerializer)}
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def management_update(request, pk):
    try:
        management = Management.objects.get(pk=pk)
    except Management.DoesNotExist:
        res = {
            'msg': 'La gestion con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = ManagementSerializer(management, data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Gestion actualizada correctamente',
            'status': 200,
            'data': serializer.data
        }
        return Response(res, status=200)
    res = {
        'msg': 'Error al actualizar la gestion',
        'status': 540,
        'data': serializer.errors
    }
    return Response(res, status=540)

@swagger_auto_schema(
    method='delete',
    operation_summary="Elimina una gestion existente por ID",
    operation_description="Elimina una gestion existente por ID",
    responses={200: 'Gestion eliminada correctamente', 404: 'Gestion no encontrada', 409: 'Conflicto al eliminar la gestion'}
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def management_delete(request, pk):
    try:
        management = Management.objects.get(pk=pk)
    except Management.DoesNotExist:
        res = {
            'msg': 'La gestion con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = ManagementSerializer(management)
    serializer.delete(management)
    res = {
        'msg': 'Gestion eliminada correctamente',
        'status': 200
    }
    return Response(res, status=200)
