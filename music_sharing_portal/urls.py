
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("music_app.urls")),
    path('auth/', include("authentication_app.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

