# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import LayerThicknessMeasurement


class LayerThicknessForm(utils.ProcessForm):
    class Meta:
        model = LayerThicknessMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = LayerThicknessForm
