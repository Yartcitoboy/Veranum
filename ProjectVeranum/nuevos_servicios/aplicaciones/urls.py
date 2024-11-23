from django.urls import path, include
from .views import index, form, certificado, servicio, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index,name='index'),
    path('form/',form,name='form'),
    path('certificado/', certificado, name='certificado'),
    path('servicio/', servicio,name='servicio'),
    path('login/', login_view,name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=index), name='logout'),
]
