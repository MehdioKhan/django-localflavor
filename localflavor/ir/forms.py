"""Iran-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, RegexField, Select
from django.utils.translation import ugettext_lazy as _

nc_re = re.compile(r"^(\d{3})[-\ ]?(\d{6})[-\ ]?(\d{1})$")


class IRPostalCodeField(RegexField):
    """
    A form field that validates input as a IR. postal code.

    Valid format is XXXXXXXXXX.

    .. note::

        If you are looking for a form field with a list of IR. Postal Service
        locations please use :class:`~localflavor.ir.forms.IRPSSelect`.

    .. versionadded:: 1.1

    Whitespace around the postal code is accepted and automatically trimmed.
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXXXXXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        super(IRPostalCodeField, self).__init__(r'^\d{10}$', *args, **kwargs)

    def to_python(self, value):
        value = super(IRPostalCodeField, self).to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()


class IRNationalCodeField(CharField):
    """
    A Iran National Code.

    Checks the following rules to determine whether the number is valid:

        * Conforms to the XXX-XXXXXX-X format.
        * No group consists entirely of zeroes.

    .. versionadded:: 1.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid IR. National Code in XXX-XXXXXX-X format.'),
    }

    def clean(self, value):
        super(IRNationalCodeField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value
        match = re.match(nc_re, value)
        if not match:
            raise ValidationError(self.error_messages['invalid'])
        return '%s' % (value)
