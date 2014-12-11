from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inventory.views.home', name='inventory_home'),
    url(r'^away$', 'inventory.views.away')
)

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='dashboard_login'),

    url(r'^logout/$', 'logout',
        {'next_page': 'boardgames_home'},
        name='dashboard_logout'),
)