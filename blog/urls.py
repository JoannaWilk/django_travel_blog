from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "blog"

urlpatterns = [
    url(r'^about', views.about, name="about"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name="post_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
