from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import ProtectedError
from ..models import Library, Book, Member
from ..serializers import LibrarySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#----------------------------------------------------------------
# CRUD for Library
#----------------------------------------------------------------
@swagger_auto_schema(
    method='get',
    operation_summary="Lista todas las librerias",
    operation_description="Lista todas las librerias",
    responses={200: openapi.Response('Lista de librerias', LibrarySerializer(many=True))}
)
@api_view(['GET'])
def get_libraries(request):
    libraries = Library.objects.all()
    serializer = LibrarySerializer(libraries, many=True)
    res = {
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='get',
    operation_summary="Obtiene una libreria por su ID",
    operation_description="Obtiene una libreria por su ID",
    responses={200: openapi.Response('Libreria encontrada', LibrarySerializer)}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_library_pk(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        res = {            
            'msg': 'La libreria con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = LibrarySerializer(library)
    res = {
        'msg': 'Libreria encontrada',
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='post',
    operation_summary="Crea una nueva libreria",
    operation_description="Crea una nueva libreria",
    request_body=LibrarySerializer,
    responses={201: openapi.Response('Libreria creada correctamente', LibrarySerializer)}
)
@api_view(['POST'])
def new_library(request):
    serializer = LibrarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Libreria creada correctamente',
            'status': 201,
            'data': serializer.data
        }
        return Response(res, status=200)
    res = {
        'msg': 'Error al crear la libreria',
        'status': 409,
        'data': serializer.errors
    }
    return Response(res, status=409)

@swagger_auto_schema(
    method='put',
    operation_summary="Actualiza una libreria existente por ID",
    operation_description="Actualiza una libreria existente por ID",
    request_body=LibrarySerializer,
    responses={200: openapi.Response('Libreria actualizada correctamente', LibrarySerializer)}
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_library(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        res = {
            'msg': 'La libreria con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res,status=404)
    serializer = LibrarySerializer(library, data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Libreria actualizada correctamente',
            'status': 200,
            'data': serializer.data
        }
        return Response(res, status=200)
    return Response(serializer.errors, status=400)

@swagger_auto_schema(
    method='delete',
    operation_summary="Elimina una libreria existente por ID",
    operation_description="Elimina una libreria existente por ID",
    responses={200: 'Libreria eliminada correctamente', 404: 'Libreria no encontrada', 409: 'Conflicto al eliminar la libreria'}
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_library(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        res = {
            'msg': 'La libreria con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res,status=404)
    try:
        library.delete()
        res = {
            'msg': 'Libreria eliminada correctamente',
            'status': 200
        }
        return Response(res,status=200)
    except ProtectedError as e:
        protected_objects = e.protected_objects
        member_count = sum(1 for obj in protected_objects if isinstance(obj, Member))
        books_count = sum(1 for obj in protected_objects if isinstance(obj, Book))
        res = {
            'msg': f'No se puede eliminar la libreria porque tiene {member_count} miembros y {books_count} libros asociados.',
            'status': 409
        }
        return Response(res, status=409)