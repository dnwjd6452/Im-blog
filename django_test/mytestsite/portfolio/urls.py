from django.urls import path, include
from . import views

urlpatterns = [
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
]