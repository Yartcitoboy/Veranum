from django.urls import path, include
from .views import index, form, certificado, servicio

urlpatterns = [
    path('', index,name='index'),
    path('form/',form,name='form'),
    path('certificado/', certificado, name='certificado'),
    path('servicio/', servicio,name='servicio'),
]
