from django.conf.urls import include, url
import django.contrib.auth.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/login/$', django.contrib.auth.views.login,name='login'),
    url(r'^account/logout/$', django.contrib.auth.views.logout,name='logout',kwargs={'next_page':'/'}),
    url(r'',include('blog.urls')),
]
