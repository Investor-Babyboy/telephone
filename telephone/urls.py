from .views import homepage, add, cancel, alter
from django.urls import path

urlpatterns = [
    path('homepage', homepage, name='homepage'),
    path('add', add, name='add'),
    path('cancel/<int:id>', cancel, name='cancel'),
    path('alter/<int:id>', alter, name='alter'),
]