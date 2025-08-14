from django.urls import path
from app.views.managements import *

urlpatterns = [
    # Management URLs
    path('', management_list, name='management-list'),
    path('<int:pk>/detail', management_detail, name='management-detail'),
    path('new/', management_create, name='management-create'),
    path('<int:pk>/edit/', management_update, name='management-update'),
    path('<int:pk>/delete/', management_delete, name='management-delete'),

]