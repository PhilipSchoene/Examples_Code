# This file is part of JuliaBase.

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


class DecimalQuantityField(models.DecimalField):
    description = _("Fixed-point number in the unit of %(unit)s")

    def __init__(self, *args, **kwargs):
        self.unit = kwargs.pop("unit", None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        result = super().formfield(**kwargs)
        result.unit = self.unit
        return result


class FloatQuantityField(models.FloatField):
    description = _("Floating-Point number in the unit of %(unit)s")

    def __init__(self, *args, **kwargs):
        self.unit = kwargs.pop("unit", None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        result = super().formfield(**kwargs)
        result.unit = self.unit
        return result


class IntegerQuantityField(models.IntegerField):
    description = _("Integer in the unit of %(unit)s")

    def __init__(self, *args, **kwargs):
        self.unit = kwargs.pop("unit", None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        result = super().formfield(**kwargs)
        result.unit = self.unit
        return result


class PositiveIntegerQuantityField(models.PositiveIntegerField):
    description = _("Positive integer in the unit of %(unit)s")

    def __init__(self, *args, **kwargs):
        self.unit = kwargs.pop("unit", None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        result = super().formfield(**kwargs)
        result.unit = self.unit
        return result


class SmallIntegerQuantityField(models.SmallIntegerField):
    description = _("Small integer in the unit of %(unit)s")

    def __init__(self, *args, **kwargs):
        self.unit = kwargs.pop("unit", None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        result = super().formfield(**kwargs)
        result.unit = self.unit
        return result


class PositiveSmallIntegerQuantityField(models.PositiveSmallIntegerField):
    description = _("Positive small integer in the unit of %(unit)s")

    def __init__(self, *args, **kwargs):
        self.unit = kwargs.pop("unit", None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        result = super().formfield(**kwargs)
        result.unit = self.unit
        return result


_ = ugettext
