from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'inRange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^$', 'twitter.views.hello', name='home'),
    url(r'^tweets/', 'twitter.views.tweets', name="tweets"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
