from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('edit_portfolio', views.edit_portfolio, name='edit_portfolio'),
    path('showcase/', views.project_showcase_view, name='project_showcase'),
]
