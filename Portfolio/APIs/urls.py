from django.urls import path
from .views import PortfolioListCreateAPIView, PortfolioRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('portfolio/', PortfolioListCreateAPIView.as_view(), name='portfolio-list-create'),
    path('portfolio/<int:pk>/', PortfolioRetrieveUpdateDestroyAPIView.as_view(), name='portfolio-retrieve-update-destroy'),
]
