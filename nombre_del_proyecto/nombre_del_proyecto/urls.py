from django.contrib import admin
from django.urls import include, path
from nombre_de_la_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('tipodocumentos/crear/', views.crear_tipodocumento, name='crear_tipodocumento'),
    path('tipodocumentos/lista/', views.lista_tipodocumentos, name='lista_tipodocumentos'),
    path('tipodocumentos/actualizar/<int:tipodocumento_id>/', views.actualizar_tipodocumento, name='actualizar_tipodocumento'),
    path('tipodocumentos/eliminar/<int:tipodocumento_id>/', views.eliminar_tipodocumento, name='eliminar_tipodocumento'),
]
