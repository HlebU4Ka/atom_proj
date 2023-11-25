from django.core.exceptions import ValidationError


def validate_related_habit(value):
    if value.is_rewarding_habit:
        raise ValidationError("Связанная с этой привычкой не может быть полезной")


def validate_time_required(value):
    if value > 120:
        raise ValidationError("Требуемое время не может превышать 120 секунд")
