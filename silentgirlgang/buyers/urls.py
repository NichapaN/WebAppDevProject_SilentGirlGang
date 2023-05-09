from django.urls import path, re_path
from . import views

# URLConf
urlpatterns = [
    # path('product/', views.product),
    # path('', views.store),
    path('profile/', views.Profileview.as_view(), name='profile'),
    #path('adress/', views.Profileview, name='profile')
]
