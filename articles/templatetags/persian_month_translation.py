from django import template

register = template.Library()


@register.filter
def translate_month(value):
    value = str(value)
    english_to_persian_month = value.maketrans(
        'Aban', 'آبان',

    )
    return value.translate(english_to_persian_month)
