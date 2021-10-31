
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.site.site_header = 'ImageBazzar'
admin.site.index_title = 'ImageBazzar | Admin'
admin.site.site_title = 'ImageBazzar'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imgpro.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
