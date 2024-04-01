# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import FTIRMeasurement


class FTIRMeasurementForm(utils.ProcessForm):
    class Meta:
        model = FTIRMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = FTIRMeasurementForm
