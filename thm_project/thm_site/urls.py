# This file is part of JuliaBase-Institute

"""Root URL dispach for the JuliaBase installation.  Mapping URL patterns to
function calls.  This is the local URL dispatch of the Django application
“jb_common”, which provides core functionality and core views for all JuliaBase
apps.

:var urlpatterns: the actual mapping.  See the `Django documentation`_ for
  details.

.. _Django documentation:
    http://docs.djangoproject.com/en/dev/topics/http/urls/
"""

from django.urls import include, re_path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
import oai_pmh.urls, institute.urls, jb_common.urls, samples.urls


urlpatterns = [
#    re_path(r"^oai-pmh", include(oai_pmh.urls)),
    re_path(r"", include(institute.urls)),
    re_path(r"", include(jb_common.urls)),
    re_path(r"", include(samples.urls)),

    re_path(r"^admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
