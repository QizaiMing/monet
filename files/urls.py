from django.urls import path
from .views import api_detail_file

app_name = "files"
urlpatterns = [path("file/<int:id_>", api_detail_file, name="detail")]
