from django.conf.urls import include, url
# Setup Django admin to work with Misago auth
from django.contrib import admin

from misago.users.forms.auth import AdminAuthenticationForm

from ..views import javascript_catalog, momentjs_catalog
from . import views


admin.autodiscover()
admin.site.login_form = AdminAuthenticationForm



urlpatterns = [
    url(r'^forum/', include('misago.urls', namespace='misago')),
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^django-i18n.js$', javascript_catalog, name='django-i18n'),
    url(r'^moment-i18n.js$', momentjs_catalog, name='moment-i18n'),

    url(r'^forum/test-mail-user/$', views.test_mail_user, name='test-mail-user'),
    url(r'^forum/test-mail-users/$', views.test_mail_users, name='test-mail-users'),
    url(r'^forum/test-pagination/$', views.test_pagination, name='test-pagination'),
    url(r'^forum/test-pagination/(?P<page>[1-9][0-9]*)/$', views.test_pagination, name='test-pagination'),
    url(r'^forum/test-paginated-response/$', views.test_paginated_response, name='test-paginated-response'),
    url(r'^forum/test-paginated-response-data/$', views.test_paginated_response_data, name='test-paginated-response-data'),
    url(r'^forum/test-paginated-response-serializer/$', views.test_paginated_response_serializer, name='test-paginated-response-serializer'),
    url(r'^forum/test-paginated-response-data-serializer/$', views.test_paginated_response_data_serializer, name='test-paginated-response-data-serializer'),
    url(r'^forum/test-paginated-response-data-extra/$', views.test_paginated_response_data_extra, name='test-paginated-response-data-extra'),
    url(r'^forum/test-valid-slug/(?P<slug>[a-z0-9\-]+)-(?P<pk>\d+)/$', views.validate_slug_view, name='validate-slug-view'),
    url(r'^forum/test-banned/$', views.raise_misago_banned, name='raise-misago-banned'),
    url(r'^forum/test-403/$', views.raise_misago_403, name='raise-misago-403'),
    url(r'^forum/test-404/$', views.raise_misago_404, name='raise-misago-404'),
    url(r'^forum/test-405/$', views.raise_misago_405, name='raise-misago-405'),
    url(r'^test-403/$', views.raise_403, name='raise-403'),
    url(r'^test-404/$', views.raise_404, name='raise-404'),
    url(r'^test-redirect/$', views.test_redirect, name='test-redirect'),
    url(r'^test-require-post/$', views.test_require_post, name='test-require-post'),
]
