from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, {"template": 'index.html'}),

    (r'^history/$', 'history.views.show'),
    (r'^projects/$', 'projects.views.show_all'),

    (r'^site_media/(.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)

