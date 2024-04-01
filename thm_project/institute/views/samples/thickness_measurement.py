# This file is part of JuliaBase-Institute

import samples.utils.views as utils
from institute.models import ThicknessMeasurement


class ThicknessForm(utils.ProcessForm):
    class Meta:
        model = ThicknessMeasurement
        fields = "__all__"


class EditView(utils.ProcessView):
    form_class = ThicknessForm
