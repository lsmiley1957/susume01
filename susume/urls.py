from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Susume", api.SusumeViewSet)
router.register("Susupmt", api.SusupmtViewSet)
router.register("Susutype", api.SusutypeViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("susume/Susume/", views.SusumeListView.as_view(), name="susume_Susume_list"),
    path("susume/Susume/create/", views.SusumeCreateView.as_view(), name="susume_Susume_create"),
    path("susume/Susume/detail/<int:pk>/", views.SusumeDetailView.as_view(), name="susume_Susume_detail"),
    path("susume/Susume/update/<int:pk>/", views.SusumeUpdateView.as_view(), name="susume_Susume_update"),
    path("susume/Susume/delete/<int:pk>/", views.SusumeDeleteView.as_view(), name="susume_Susume_delete"),
    path("susume/Susupmt/", views.SusupmtListView.as_view(), name="susume_Susupmt_list"),
    path("susume/Susupmt/create/", views.SusupmtCreateView.as_view(), name="susume_Susupmt_create"),
    path("susume/Susupmt/detail/<int:pk>/", views.SusupmtDetailView.as_view(), name="susume_Susupmt_detail"),
    path("susume/Susupmt/update/<int:pk>/", views.SusupmtUpdateView.as_view(), name="susume_Susupmt_update"),
    path("susume/Susupmt/delete/<int:pk>/", views.SusupmtDeleteView.as_view(), name="susume_Susupmt_delete"),
    path("susume/Susutype/", views.SusutypeListView.as_view(), name="susume_Susutype_list"),
    path("susume/Susutype/create/", views.SusutypeCreateView.as_view(), name="susume_Susutype_create"),
    path("susume/Susutype/detail/<int:pk>/", views.SusutypeDetailView.as_view(), name="susume_Susutype_detail"),
    path("susume/Susutype/update/<int:pk>/", views.SusutypeUpdateView.as_view(), name="susume_Susutype_update"),
    path("susume/Susutype/delete/<int:pk>/", views.SusutypeDeleteView.as_view(), name="susume_Susutype_delete"),

    path("susume/htmx/Susume/", htmx.HTMXSusumeListView.as_view(), name="susume_Susume_htmx_list"),
    path("susume/htmx/Susume/create/", htmx.HTMXSusumeCreateView.as_view(), name="susume_Susume_htmx_create"),
    path("susume/htmx/Susume/delete/<int:pk>/", htmx.HTMXSusumeDeleteView.as_view(), name="susume_Susume_htmx_delete"),
    path("susume/htmx/Susupmt/", htmx.HTMXSusupmtListView.as_view(), name="susume_Susupmt_htmx_list"),
    path("susume/htmx/Susupmt/create/", htmx.HTMXSusupmtCreateView.as_view(), name="susume_Susupmt_htmx_create"),
    path("susume/htmx/Susupmt/delete/<int:pk>/", htmx.HTMXSusupmtDeleteView.as_view(), name="susume_Susupmt_htmx_delete"),
    path("susume/htmx/Susutype/", htmx.HTMXSusutypeListView.as_view(), name="susume_Susutype_htmx_list"),
    path("susume/htmx/Susutype/create/", htmx.HTMXSusutypeCreateView.as_view(), name="susume_Susutype_htmx_create"),
    path("susume/htmx/Susutype/delete/<int:pk>/", htmx.HTMXSusutypeDeleteView.as_view(), name="susume_Susutype_htmx_delete"),
)