from django.urls import path, re_path
from . import views

# URLConf
urlpatterns = [
    # path('product/', views.product),
    path('', views.frontpage),
]

