"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ~/projects/django-web-app/merchex/merchex/urls.py

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    # ajouter ce motif sous notre autre motif de groupes
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/update/', views.band_update, name='band-update'),



    path('comics/', views.about, name='comic-list'),  # ajoutez cette ligne
    path('comics/<int:id>/', views.comic_detail, name='comic-detail'),
    path('comics/create/', views.comic_create, name='comic-create'),
    path('comics/<int:id>/update/', views.comic_update, name='comic-update'),
    path('comics/<int:id>/delete/', views.comic_delete, name='comic-delete'),


    path('contact-us/', views.contact, name='contact'),

]
