from django.conf import settings
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('podcast_user.urls')),
    path('basic/', include('basic_pages.urls')),
    path('blog/', include('podcast_blog.urls')),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
