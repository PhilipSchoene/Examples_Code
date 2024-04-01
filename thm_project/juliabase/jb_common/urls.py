# This file is part of JuliaBase

"""Mapping URL patterns to function calls.  This is the local URL dispatch of
the Django application “jb_common”, which provides core functionality and
core views for all JuliaBase apps.

:var urlpatterns: the actual mapping.  See the `Django documentation`_ for
  details.

.. _Django documentation:
    http://docs.djangoproject.com/en/dev/topics/http/urls/

"""

from django.urls import include, re_path
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog
from django.contrib.auth import views as auth_views
from jb_common.views import show_user, markdown_sandbox, switch_language, show_error_page, hilfe


jb_common_patterns = ([
    re_path(r"^users/(?P<login_name>.+)", show_user, name="show_user"),
    re_path(r"^markdown$", markdown_sandbox, name="markdown_sandbox"),
    re_path(r"^switch_language$", switch_language, name="switch_language"),
    re_path(r"^error_pages/(?P<hash_value>.+)", show_error_page, name="show_error_page"),
    re_path(r"^hilfe$", hilfe, name="hilfe"),
    re_path(r"^jsi18n/$", cache_page(3600)(JavaScriptCatalog.as_view(packages=settings.JAVASCRIPT_I18N_APPS)), name="jsi18n"),
], "jb_common")

# Unfortunately, the ``PasswordChangeView`` view expects the
# ``PasswordChangeDoneView`` URL name to live in the global namespace,
# therefore, I have to define these separately.
login_related_patterns = [
    re_path(r"^change_password$", auth_views.PasswordChangeView.as_view(template_name="jb_common/change_password.html"),
            name="password_change"),
    re_path(r"^change_password/done/$", auth_views.PasswordChangeDoneView.as_view(
        template_name="jb_common/password_changed.html"), name="password_change_done"),
    re_path(r"^login$", auth_views.LoginView.as_view(template_name="jb_common/login.html"), name="login"),
    re_path(r"^logout$", auth_views.LogoutView.as_view(template_name="jb_common/logout.html"), name="logout"),
]

urlpatterns = [
    re_path(r"", include(login_related_patterns)),
    re_path(r"", include(jb_common_patterns)),
]
