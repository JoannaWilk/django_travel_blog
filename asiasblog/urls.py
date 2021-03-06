from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from blog import views

urlpatterns = [
    url(r'^thisisfreakingvirus/', admin.site.urls),
    # url(r'^$', views.post_list, name="post_list"),
    url(r'^$', views.PostListView.as_view(), name="home"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
