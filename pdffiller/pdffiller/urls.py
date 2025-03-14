from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_client, name="create_client"),
    path(
        "download/<str:company_name>/<str:template_name>",
        views.download_pdf,
        name="download_pdf",
    ),
]
