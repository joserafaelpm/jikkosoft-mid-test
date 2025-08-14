from django.urls import path
from app.views.members import *

urlpatterns = [
    # Member URLs
    path('', member_list, name='member-list'),
    path('<int:pk>/detail', member_detail, name='member-detail'),
    path('new/', member_create, name='member-create'),
    path('<int:pk>/edit/', member_update, name='member-update'),
    path('<int:pk>/delete/', member_delete, name='member-delete'),

]