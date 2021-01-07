from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns 
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView


# Uncomment the next two lines to enable the admin:
admin.autodiscover()
admin.site.enable_nav_sidebar = False

admin.site.site_header = 'Software de Historias Clinicas'
admin.site.site_title = 'Historias Clinicas'
admin.site.index_title = "Bienvenido al Software de Historias Clinicas"


urlpatterns = i18n_patterns(
    # Examples:
    # url(r'^$', 'hist.views.home', name='home'),
    # url(r'^hist/', include('hist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path('', RedirectView.as_view(url='/admin')),
    path('admin/historias/', include('historias.urls')),
    path('admin/', admin.site.urls),

)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns