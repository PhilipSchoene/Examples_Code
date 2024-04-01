# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import LPSMeasurement


class LPSMeasurementForm(utils.ProcessForm):
    class Meta:
        model = LPSMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = LPSMeasurementForm
