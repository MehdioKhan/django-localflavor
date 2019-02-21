from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _
from .forms import IRPostalCodeField as IRPostalCodeFormField
from .forms import IRNationalCodeField as IRNationalCodeFormField


class IRPostalCodeField(CharField):
    """
    A model field that stores the IR. postal code in the database.

    Forms represent it as a :class:`~localflavor.ir.forms.IRPostalCodeField` field.

    .. note::

        If you are looking for a model field with a list of U.S. Postal Service
        locations please use :class:`~localflavor.ir.models.IRPostalCodeField`.

    .. versionadded:: 1.1

    """

    description = _("IR. postal code")

    def __init__(self, *args, **kwargs):
        super(IRPostalCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': IRPostalCodeFormField}
        defaults.update(kwargs)
        return super(IRPostalCodeField, self).formfield(**defaults)


class IRNationalCodeField(CharField):
    """
    A model field that stores  the national code in the format ``XXX-XXXXXX-X``.

    Forms represent it as ``forms.IRNationalCodeField`` field.

    .. versionadded:: 1.1
    """

    description = _("National code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(IRNationalCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': IRNationalCodeFormField}
        defaults.update(kwargs)
        return super(IRNationalCodeField, self).formfield(**defaults)
