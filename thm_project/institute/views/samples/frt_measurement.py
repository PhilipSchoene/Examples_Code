# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import FRTMeasurement


class FRTMeasurementForm(utils.ProcessForm):
    class Meta:
        model = FRTMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = FRTMeasurementForm
