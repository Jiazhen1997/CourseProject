
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rake_app import views as rake_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', rake_views.MainView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name="a"b"o"u"t"."h"t"m"l"")"")""
""]""
""
