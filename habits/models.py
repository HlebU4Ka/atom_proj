from django.db import models
from settings_app import settings
from django.core.exceptions import ValidationError

from settings_app.validators import validate_related_habit, validate_time_required


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Habit(models.Model):
    """
        Модель, представляющая привычку пользователя.

        Поля:
        - user: Внешний ключ на пользователя, который создал привычку.
        - place: Место, связанное с привычкой.
        - time: Время, когда выполняется привычка.
        - action: Описание самой привычки.
        - is_rewarding_habit: Флаг, указывающий, является ли привычка вознаграждением.
        - related_habit: Связь с другой привычкой.
        - frequency: Частота выполнения привычки (по умолчанию 1).
        - reward: Описание вознаграждения за выполнение привычки.
        - time_required: Время, требуемое для выполнения привычки.
        - is_public: Флаг, указывающий, является ли привычка общедоступной.
        - status: Статус привычки.

        Методы:
        - __str__: Возвращает описание привычки в виде строки.

        """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    time = models.TimeField()
    action = models.CharField(max_length=200)
    is_rewarding_habit = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, validators=[validate_related_habit])
    time_required = models.PositiveIntegerField(validators=[validate_time_required])
    frequency = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Выполняем валидацию перед сохранением привычки
        self.full_clean()
        super(Habit, self).save(*args, **kwargs)

    def clean(self):
        # Валидация связанной с привычкой привычки
        if self.related_habit and self.related_habit.is_rewarding_habit:
            raise ValidationError("Связанная с этой привычкой не может быть полезной", code='invalid_related_habit')
        # Валидация времени, требуемого для выполнения привычки
        if self.time_required > 120:
            raise ValidationError("Требуемое время не может превышать 120 секунд", code='invalid_time_required')
        # Валидация частоты выполнения привычки
        if self.frequency < 7:
            raise ValidationError("Периодичность применения привычки не может быть менее 7 дней.",
                                  code='invalid_frequency')
        # Валидация вознаграждающей привычки
        if self.is_rewarding_habit and (self.reward or self.related_habit):
            raise ValidationError(
                "Вознаграждающая привычка не может иметь вознаграждения или связанной с ней привычки.",
                code='invalid_rewarding_habit')
        # Валидация общественной привычки
        if self.is_public and (self.is_rewarding_habit or self.related_habit):
            raise ValidationError("Общественная привычка не может быть полезной или иметь связанную с ней привычку.",
                                  code='invalid_public_habit')

    def __unicode__(self):
        return self.action