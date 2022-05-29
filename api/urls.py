from django.urls import path, include
from .views import *

urlpatterns = [
    path("hello/", HelloAPI),
    path("test/", upload_file),

]