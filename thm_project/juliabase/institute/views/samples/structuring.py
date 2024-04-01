# This file is part of JuliaBase-Institute

from django.utils.translation import ugettext_lazy as _, ugettext
import samples.utils.views as utils
import institute.models as institute_models


class StructuringForm(utils.ProcessForm):
    class Meta:
        model = institute_models.Structuring
        fields = "__all__"


class EditView(utils.RemoveFromMySamplesMixin, utils.ProcessView):
    form_class = StructuringForm


_ = ugettext
