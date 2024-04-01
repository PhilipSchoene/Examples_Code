# This file is part of JuliaBase-Institute

"""Views to add and edit substrates.
"""

from django.db.models import Max
from django.forms.utils import ValidationError
from django.utils.translation import ugettext_lazy as _, ugettext, ugettext
from institute import models as institute_models
import samples.utils.views as utils


class SubstrateForm(utils.ProcessForm):

    class Meta:
        model = institute_models.Substrate
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("material") == "custom" and not cleaned_data.get("comments"):
            self.add_error("comments", ValidationError(_("For a custom substrate, you must give substrate comments."),
                                                       code="required"))
        return cleaned_data


class EditView(utils.ProcessMultipleSamplesView):
    form_class = SubstrateForm

    def is_referentially_valid(self):
        """Test whether a sample has more than one substrate or whether the substrate
        is not the very first process.

        :return:
          whether all forms are consistent with each other and the database

        :rtype: bool
        """
        referentially_valid = super().is_referentially_valid()
        if self.forms["samples"].is_valid() and self.forms["process"].is_valid():
            for sample in self.forms["samples"].cleaned_data["sample_list"]:
                processes = sample.processes
                if processes.exists():
                    earliest_timestamp = processes.aggregate(Max("timestamp"))["timestamp__max"]
                    if earliest_timestamp < self.forms["process"].cleaned_data["timestamp"]:
                        self.forms["samples"].add_error(
                            "sample_list", _("Sample {0} has already processes before the timestamp of this substrate, "
                                             "namely from {1}.").format(sample, earliest_timestamp))
                        referentially_valid = False
                    for process in processes.all():
                        if process.content_type.model_class() == institute_models.Substrate:
                            self.forms["samples"].add_error(
                                "sample_list", _("Sample {0} has already a substrate.").format(sample))
                            referentially_valid = False
                            break
        return referentially_valid


_ = ugettext
