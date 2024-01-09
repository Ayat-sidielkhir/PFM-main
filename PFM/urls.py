from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Use a different path for the home view
    path('store/', include('store.urls')),  # Use 'store/' as the path for store app
path('cart/',include('carts.urls')),

]
# Configuration pour servir les fichiers médias pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
