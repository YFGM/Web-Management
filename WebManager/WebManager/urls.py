from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Admin.views.index', name='index'),
    url(r'^admin/', include('Admin.urls')),
)
