from django.urls import path
from webapp.views import start, cat_info


urlpatterns = [
    path('', start, name='start'),
    path('cat_info/', cat_info, name='cat_info')
]