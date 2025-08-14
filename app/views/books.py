from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import ProtectedError
from ..models import Book, Management
from ..serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#----------------------------------------------------------------
# CRUD for Book
#----------------------------------------------------------------
@swagger_auto_schema(
    method='get',
    operation_summary="Obtener lista de libros",
    operation_description="Lista todos los libros",
    responses={200: openapi.Response('Lista de libros', BookSerializer(many=True))}
)
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    res = {
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='get',
    operation_summary="Obtiene un libro por su ID",
    operation_description="Obtiene un libro por su ID",
    responses={200: openapi.Response('Libro encontrado', BookSerializer)}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        res = {
            'msg': 'El libro con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = BookSerializer(book)
    res = {
        'msg': 'Libro encontrado',
        'status': 200,
        'data': serializer.data
    }
    return Response(res, status=200)

@swagger_auto_schema(
    method='post',
    operation_summary="Crea un nuevo libro",
    operation_description="Crea un nuevo libro",
    request_body=BookSerializer,
    responses={201: openapi.Response('Libro creado correctamente', BookSerializer)}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Libro creado correctamente',
            'status': 201,
            'data': serializer.data
        }
        return Response(res, status=201)
    res = {
        'msg': 'Error al crear el libro',
        'status': 400,
        'errors': serializer.errors
    }
    return Response(res, status=400)

@swagger_auto_schema(
    method='put',
    operation_summary="Actualiza un libro existente por ID",
    operation_description="Actualiza un libro existente",
    request_body=BookSerializer,
    responses={200: openapi.Response('Libro actualizado correctamente', BookSerializer)}
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def book_update(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        res = {
            'msg': 'El libro con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {
            'msg': 'Libro actualizado correctamente',
            'status': 200,
            'data': serializer.data
        }
        return Response(res, status=200)
    res = {
        'msg': 'Error al actualizar el libro',
        'status': 400,
        'errors': serializer.errors
    }
    return Response(res, status=400)

@swagger_auto_schema(
    method='delete',
    operation_summary="Elimina un libro existente por ID",
    operation_description="Elimina un libro existente por ID",
    responses={200: 'Libro eliminado correctamente', 404: 'Libro no encontrado', 409: 'Conflicto al eliminar el libro'}
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def book_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        res = {
            'msg': 'El libro con id {} no existe'.format(pk),
            'status': 404
        }
        return Response(res, status=404)
    try:
        book.delete()
        res = {
            'msg': 'Libro eliminado correctamente',
            'status': 200
        }
        return Response(res, status=200)
    except ProtectedError as e:
        management_count = Management.objects.filter(book_id=pk).count()
        res = {
            'msg': f'No se puede eliminar el libro porque tiene {management_count} gestiones asociadas.',
            'status': 409
        }
        return Response(res, status=409)