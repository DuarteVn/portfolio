
from django.contrib import admin
from django.urls import path, include
from app_pt import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('app_pt/', include('app_pt.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])