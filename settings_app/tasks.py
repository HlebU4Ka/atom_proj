from celery import shared_task
from .telegram_utils import send_telegram_notification
from habits.models import Habit


@shared_task
def send_habit_notification(habit_id):
    habit = Habit.objects.get(id=habit_id)
    # Подготовьте сообщение для уведомления
    message = f"Напоминание: Вы должны выполнить привычку '{habit.action}' сейчас!"
    # Отправьте уведомление в Telegram
    send_telegram_notification(habit.user.telegram_chat_id, message)
