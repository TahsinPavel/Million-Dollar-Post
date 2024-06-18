from django.urls import path
from .views import HomeView, AirticleDetailview

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('airticle/<int:pk>', AirticleDetailview.as_view(), name='article-detail'),
]
