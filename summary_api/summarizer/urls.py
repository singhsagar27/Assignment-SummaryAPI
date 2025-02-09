# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import GenerateSummaryView, GenerateBulletPointsView
#
# urlpatterns = [
#     path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
#     path("generate-summary/", GenerateSummaryView.as_view(), name="generate_summary"),
#     path("generate-bullet-points/", GenerateBulletPointsView.as_view(), name="generate_bullet_points"),
# ]

from django.urls import path
from .views import GenerateSummaryView, GenerateBulletPointsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("generate-summary/", GenerateSummaryView.as_view(), name="generate_summary"),
    path("generate-bullet-points/", GenerateBulletPointsView.as_view(), name="generate_bullet_points"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
