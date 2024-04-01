# This file is part of JuliaBase.


"""Additional context processors for JuliaBase.  These functions must be added
to ``settings.TEMPLATES[…]["OPTIONS"]["context_processors"]``.  They add
further data to the dictionary passed to the templates.
"""

from django.conf import settings
from django.utils.translation import ugettext


def default(request):
    """Injects some session data into the template context.

    The help link on the top (see the `samples.utils.views.help_link`
    decorator) is added to the context by extracting it (and removing it from)
    the request object.

    Moreover, it adds tuples with information needed to realise the neat little
    flags on the top left for language switching.  These flags don't occur if
    it was a POST request, or if the user isn't logged-in.

    :param request: the current HTTP Request object

    :type request: HttpRequest

    :return:
      the (additional) context dictionary

    :rtype: dict mapping str to session data
    """
    user = request.user
    result = {}
    try:
        result["help_link"] = settings.HELP_LINK_PREFIX + request.juliabase_help_link
    except AttributeError:
        pass
    result["url"] = request.path
    if request.GET:
        result["url"] += "?" + request.GET.urlencode()
    if user.is_authenticated:
        result["salutation"] = user.first_name or user.username
    if request.method == "GET":
        result["translation_flags"] = tuple((code, ugettext(language)) for code, language in settings.LANGUAGES)
    else:
        result["translation_flags"] = ()
    result["default_home_url"] = settings.LOGIN_REDIRECT_URL
    result["add_samples_view"] = settings.ADD_SAMPLES_VIEW
    return result
