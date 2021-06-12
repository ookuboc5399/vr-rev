from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('Concept/', views.CONCEPTView.as_view(), name='Concept'),
    path('Product/', views.PRODUCTView.as_view(), name='Product'),
    path('Blog/', views.BLOGView.as_view(), name='Blog'),
    path('post/<int:pk>/', views.BLOGDetailView.as_view(), name='post_detail'),
    path('contact/', views.CONTACTView.as_view(), name='contact'),
]