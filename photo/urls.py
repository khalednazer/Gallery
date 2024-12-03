from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', one, name='homee'),
    path('create/', create, name='creates'),
    path('photo/', pht, name='photoss'),
    path('onephoto/<str:slug>', photslug, name='onephotoo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )



# https://github.com/khalednazer/portfolio_project/blob/main/Portfolio/settings.py
# https://www.youtube.com/watch?v=sSquD2u5Ie0&list=PL-51WBLyFTg38qZ0KHkJj-paDQAAu9HiP&index=14&ab_channel=DennisIvy
# https://chatgpt.com/c/674aa662-7080-8003-9b40-be7c3154c902