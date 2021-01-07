from django.urls import path

from historias import views

urlpatterns = [
 #   path('', views.historia_report, name='historia_report')
 	 path('medico/<path:object_id>/reporte/', views.medico_report, name='medico_report')
]