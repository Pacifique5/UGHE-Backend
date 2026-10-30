from django.urls import path

from content.views import HomepageView

urlpatterns = [
    path("homepage/", HomepageView.as_view(), name="homepage"),
]
