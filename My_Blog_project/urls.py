from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('app_login.urls')),
    path('blog', include('app_blog.urls')),
    path('', views.index,name= 'index'),
]

urlpatterns += static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static (settings.STATIC_URL, document_root= settings.STATIC_ROOT)
