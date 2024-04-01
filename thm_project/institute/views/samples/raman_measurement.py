# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import RamanMeasurement


class RamanForm(utils.ProcessForm):
    class Meta:
        model = RamanMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = RamanForm
