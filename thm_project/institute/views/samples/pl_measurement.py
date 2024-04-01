# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import PLMeasurement


class PLMeasurementForm(utils.ProcessForm):
    class Meta:
        model = PLMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = PLMeasurementForm
