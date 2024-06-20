from django.urls import path
from .views import HomeView, AirticleDetailview, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('airticle/<int:pk>', AirticleDetailview.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name= 'Add_Post'),
    path('airticle/edit/<int:pk>', UpdatePostView.as_view(), name= 'Update_Post'),
    path('airticle/<int:pk>/remove', DeletePostView.as_view(), name= 'Delete_Post'),
]
