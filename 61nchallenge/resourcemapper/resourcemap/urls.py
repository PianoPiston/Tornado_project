"""
URL configuration for resource_map project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from resource_map import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('resourcemap.urls'))
    # 1. This URL corresponds to the root of the included path (which is the root of the site: '/')
    # This is your main map view.
    path('', views.welcome_view, name='welcome_view'),
    path('map/', views.map_view, name='map_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    # 2. This URL corresponds to '/add/'
    path('add/', views.add_resource_view, name='add_resource_view'),
    path("update_status/<str:resource_type>/<int:resource_id>/", views.update_status, name="update_status"),
]
