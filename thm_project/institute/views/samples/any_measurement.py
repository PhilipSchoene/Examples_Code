# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import AnyMeasurement


class AnyMeasurementForm(utils.ProcessForm):
    class Meta:
        model = AnyMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = AnyMeasurementForm
