from django.contrib import admin
from django.conf.urls import patterns, include, url


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^', include('apps.static_pages.urls')),
    url(r"^account/", include("account.urls")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
