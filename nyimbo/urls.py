from django.urls import path

from nyimbo import views

app_name = 'nyimbo'

urlpatterns = [
    path('', views.index, name='home'),
    path('funsa/', views.funsa, name='funsa'),
    # path('search/', views.search, name='search'),
    # path('sumu/', views.sumu, name='sumu'),
    # path('nyimbo/', views.nyimbo, name='nyimbo'),
]