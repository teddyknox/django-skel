from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# serving up static pages with RequestContext variables
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
)