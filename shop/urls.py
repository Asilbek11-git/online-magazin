from django.urls import path
from . import views 

urlpatterns = [

    path('', views.index, name='index'), 

    path('savatga-qoshish/<int:mahsulot_id>/', views.savatga_qoshish, name='savatga_qoshish'),
    



]