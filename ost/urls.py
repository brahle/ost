from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'runner.views.main'),
    url(r'^(?P<start_speed>\d+\.\d+)/$', 'runner.views.main'),
    url(r'^run/(?P<parametar>\d+)/$', 'runner.views.run'),
)
