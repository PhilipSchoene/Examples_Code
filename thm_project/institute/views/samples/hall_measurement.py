# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import HallMeasurement


class HallForm(utils.ProcessForm):
    class Meta:
        model = HallMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = HallForm
