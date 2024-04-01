# This file is part of JuliaBase-Institute

from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
import samples.utils.views as utils
from institute.models import SolarsimulatorMeasurement, SolarsimulatorCellMeasurement


class SolarsimulatorMeasurementForm(utils.ProcessForm):

    class Meta:
        model = SolarsimulatorMeasurement
        fields = "__all__"

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields["temperature"].widget.attrs.update({"size": "5"})


class SolarsimulatorCellForm(utils.SubprocessForm):
    class Meta:
        model = SolarsimulatorCellMeasurement
        exclude = ("measurement",)


class EditView(utils.SubprocessesMixin, utils.ProcessView):
    form_class = SolarsimulatorMeasurementForm
    subform_class = SolarsimulatorCellForm
    process_field, subprocess_field = "measurement", "cells"


_ = ugettext
