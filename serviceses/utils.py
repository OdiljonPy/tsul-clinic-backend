import re
from django.core.validators import ValidationError


def validate_uz_number(value):
    if re.match(r'^\+998\d{9}$', value):
        return value
    else:
        raise ValidationError("Iltimos O'zbekiston telefon raqamini kiriting!")
