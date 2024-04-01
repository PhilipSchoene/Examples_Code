# This file is part of JuliaBase-Institute

"""Permission checking for special institute extensions.  It is an extension to
:py:mod:`samples.permissions`.  See there for further information.
"""

from django.utils.translation import ugettext as _
from samples.permissions import PermissionError


def assert_can_add_edit_substrate(user, substrate=None, affected_samples=None):
    """Tests whether the user can add or edit a substrate to *already
    existing* samples.  This is not used if samples and substrate process are
    created in the same request.

    :param user: the user whose permission should be checked
    :param substrate: the substrate process to be edited; ``None`` if the user
        wants to create one
    :param affected_samples: the samples that belong to the newly created
        substrate process; ``None`` if the user wants to edit one

    :type user: django.contrib.auth.models.User
    :type substrate: `institute.models.Substrate`
    :type affected_samples: list of `samples.models.Sample`

    :raises PermissionError: if the user is not allowed to add or edit the
        substrate process for those samples
    """
    assert (substrate and affected_samples is None) or (substrate is None and affected_samples is not None)
    if substrate:
        affected_samples = substrate.samples.all()
    for sample in affected_samples:
        if sample.currently_responsible_person != user:
            if substrate:
                description = _("You are not allowed to edit the substrate #{number} because you are not allowed to edit "
                                "all affected samples.").format(substrate.pk)
            else:
                description = _("You are not allowed to add a substrate because you are not allowed to edit all "
                                "affected samples.")
            raise PermissionError(user, description, new_topic_would_help=True)


# Now, I inject the ``has_permission_to_...`` functions into this module for
# for every ``assert_can_...`` function found here.
#
# FixMe: This is copied from `samples.permissions`.  Maybe it should be move to
# jb_common.

def generate_permission_function(assert_func):
    def has_permission(*args, **kwargs):
        try:
            assert_func(*args, **kwargs)
        except PermissionError:
            return False
        else:
            return True
    return has_permission


import copy, inspect
_globals = copy.copy(globals())
all_assertion_functions = [func for func in _globals.values()
                           if inspect.isfunction(func) and func.__name__.startswith("assert_can_")]
for func in all_assertion_functions:
    new_name = "has_permission_to_" + func.__name__[len("assert_can_"):]
    globals()[new_name] = generate_permission_function(func)
