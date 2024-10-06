from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.profile, name='profile'),
    # path('', views.billing, name='billing'),
    path('', views.tables, name='tables'),
    path('', views.virtualreality, name='virtual-reality'),
    path('', views.rtl, name='rtl'),
]
