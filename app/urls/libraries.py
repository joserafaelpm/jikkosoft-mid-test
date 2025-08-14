from django.urls import path
from app.views.libraries import *

urlpatterns = [
    # Library URLs
    path('', get_libraries, name='library-list'),
    path('<int:pk>/detail/', get_library_pk, name='library-detail'),
    path('new/', new_library, name='library-create'),
    path('<int:pk>/edit/', update_library, name='library-update'),
    path('<int:pk>/delete/', delete_library, name='library-delete'),
]