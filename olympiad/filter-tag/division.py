from django.template.defaulttags import register


@register.filter
def divide(value, arg):
    try:
        return round(int(value) / int(arg) * 100, 2)
    except (ValueError, ZeroDivisionError):
        return None
