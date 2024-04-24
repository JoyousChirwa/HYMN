from django.urls import path

from . import views

app_name = 'hymns'

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:header_id>/', views.details, name='details'),
    path('search/', views.search, name='search'),
    # path('sumu/', views.sumu, name='sumu'),
    # path('nyimbo/', views.nyimbo, name='nyimbo'),
]