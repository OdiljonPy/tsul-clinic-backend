import re
from django.core.validators import ValidationError


def validate_uz_number(value):
    if re.match(r'^\+998\d{9}$', value):
        return value
    else:
        raise ValidationError("Iltimos O'zbekiston telefon raqamini kiriting!")


def validate_rating(value):
    if 1 <= value <= 5:
        return value
    else:
        raise ValidationError("Rating cannot be less than 1 and greater than 5")
