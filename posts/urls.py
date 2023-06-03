from django.urls import path
from django.contrib import admin
from django.urls.conf import include  
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name = 'register'),
    path('home/', views.home, name = 'home'),
    path('auth/', views.admin, name = 'admin'),
    path('authdoubts/', views.admindoubts, name = 'admindoubts'),
    path('notifications/', views.notifications, name = 'notifications'),
    path('doubts/', views.doubts, name = 'doubts'),
    path('recents/', views.recents, name = 'recents'),
    # path('', include("posts.urls"))
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)