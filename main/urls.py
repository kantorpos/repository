import django


from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', RepoListView.as_view(), name='repo-list'),
    path('admin/', AdminListView.as_view(), name='repo-admin'),
    path("upload/", RepoUploadView.as_view(), name="repo-upload"),
    path('<int:pk>/update/', RepoUpdateView.as_view(), name='repo-update'),
]
