from django.contrib import admin
from django.urls import path

from core.views import all_matches, match_scores

urlpatterns = [
    path("admin/", admin.site.urls),
    path("matches/", all_matches, name="all_matches"),
    path("matches/<mid>", match_scores),
]
