from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = [
	url(r'^', include('blog.urls', namespace = "blog_app")),
    url(r'^admin/', include(admin.site.urls)),
]
