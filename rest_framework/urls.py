"""
Login and logout views for the browsable API.

Add these to your root URLconf if you're using the browsable API and
your API requires authentication:

    urlpatterns = [
        ...
        url(r'^auth/', include('rest_framework_tm.urls', namespace='rest_framework_tm'))
    ]

The urls must be namespaced as 'rest_framework_tm', and you should make sure
your authentication settings include `SessionAuthentication`.
"""
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views

template_name = {'template_name': 'rest_framework_tm/login.html'}

urlpatterns = [
    url(r'^login/$', views.login, template_name, name='login'),
    url(r'^logout/$', views.logout, template_name, name='logout'),
]
