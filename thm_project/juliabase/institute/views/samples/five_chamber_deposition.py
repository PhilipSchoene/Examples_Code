# This file is part of JuliaBase-Institute

from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from django.forms.utils import ValidationError
import samples.utils.views as utils
import institute.utils.views as form_utils
import institute.utils.base
import institute.models as institute_models


class DepositionForm(utils.DepositionForm):

    class Meta:
        model = institute_models.FiveChamberDeposition
        fields = "__all__"

    def clean_number(self):
        number = super().clean_number()
        return form_utils.clean_deposition_number_field(number, "S")

    def clean(self):
        cleaned_data = super().clean()
        if "number" in cleaned_data and "timestamp" in cleaned_data:
            if cleaned_data["number"][:2] != cleaned_data["timestamp"].strftime("%y"):
                self.add_error("number", ValidationError(_("The first two digits must match the year of the deposition."),
                               code="invalid"))
        return cleaned_data


class LayerForm(utils.SubprocessForm):

    class Meta:
        model = institute_models.FiveChamberLayer
        exclude = ("deposition",)
        widgets = {"number": forms.TextInput(attrs={"readonly": "readonly", "size": 5, "style": "font-size: large"}),
                   "h2": forms.TextInput(attrs={"size": 10}),
                   "sih4": forms.TextInput(attrs={"size": 10}),
                   "temperature_1": forms.TextInput(attrs={"size": 5}),
                   "temperature_2": forms.TextInput(attrs={"size": 5})}


class EditView(utils.RemoveFromMySamplesMixin, utils.DepositionView):
    form_class = DepositionForm
    step_form_class = LayerForm

    def get_next_id(self):
        return institute.utils.base.get_next_deposition_number("S")


_ = ugettext
