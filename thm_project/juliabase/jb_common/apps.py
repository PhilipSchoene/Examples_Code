# This file is part of JuliaBase.


import collections, urllib
from django.conf import settings
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _, ugettext, pgettext
from django.urls import reverse
import jb_common.utils.blobs
from jb_common.nav_menu import MenuItem


class JBCommonConfig(AppConfig):
    name = "jb_common"
    verbose_name = _("JuliaBase – administration")

    def ready(self):
        import jb_common.signals

        jb_common.utils.blobs.set_storage_backend()

    def build_menu(self, menu, request):
        """Contribute to the menu.  See :py:mod:`jb_common.nav_menu` for further
        information.
        """
        import jb_common.utils.base as utils

        menu.get_or_create(_("add"))
        menu.get_or_create(pgettext("top-level menu item", "explore"))
        menu.get_or_create(_("manage"))
        if request.user.is_authenticated:
            user_menu = menu.get_or_create(MenuItem(utils.get_really_full_name(request.user), position="right"))
            user_menu.add(
                _("edit preferences"),
                reverse("samples:edit_preferences", kwargs={"login_name": request.user.username}),
                "wrench")
            if request.user.has_usable_password():
                user_menu.add(_("change password"), reverse("password_change"), "option-horizontal")
            user_menu.add(_("logout"), reverse("logout"), "log-out")
        jb_menu = menu.get_or_create("JuliaBase")
        jb_menu.add(_("main menu"), reverse("samples:main_menu"), "home")
        try:
            help_link = request.juliabase_help_link
        except AttributeError:
            pass
        else:
            jb_menu.add(_("help"), settings.HELP_LINK_PREFIX + help_link, "question-sign")
        jb_menu.add(_("statistics"), reverse("samples:statistics"), "stats")
        jb_menu.add(_("about"), reverse("samples:about"), "info-sign")
        if request.user.is_authenticated and request.method == "GET" and settings.LANGUAGES:
            jb_menu.add_separator()
            for code, name in settings.LANGUAGES:
                back_url = request.path
                if request.GET:
                    back_url += "?" + request.GET.urlencode()
                jb_menu.add(name, "{}?lang={}&amp;next={}".format(reverse("jb_common:switch_language"), code,
                                                                  urllib.parse.quote_plus(back_url)),
                            icon_url=urllib.parse.urljoin(settings.STATIC_URL, "juliabase/flags/{}.png".format(code)),
                            icon_description=_("switch to {language}").format(language=name))


_ = ugettext
