# This file is part of JuliaBase-Institute

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _, ugettext


class InstituteConfig(AppConfig):
    name = "institute"
    verbose_name = _("Institute")

    def ready(self):
        import institute.signals
        import warnings
        warnings.filterwarnings(
                'error', r"DateTimeField .* received a naive datetime",
                RuntimeWarning, r'django\.db\.models\.fields')

_ = ugettext
