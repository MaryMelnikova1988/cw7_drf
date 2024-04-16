import datetime

import requests
from celery import shared_task
from django.core.management import settings

from habits.models import Habit
from users.models import User


@shared_task
def send_message_about_habits():
    current_time = datetime.datetime.now().time

    habits = Habit.objects.all().filter(time__lte=current_time,is_pleasant_habit=False)

    for habit in habits:
        if habit.owner.telegram_id:
            URL = 'https://api.telegram.org/bot'
            TOKEN = settings.TELEGRAM_TOKEN
            message = (f'Привет, {habit.owner.email}!'
                       f'Сегодня в {habit.time} в {habit.place}'
                       f'тебе надо выполнить {habit.action} в течение {habit.duration} секунд.')
            requests.post(
                url=f'{URL}{TOKEN}/sendMessage',
                data={
                    'chat_id': habit.owner.telegram_id,
                    'text': message,
                }
            )


@shared_task
def send_mess_hello():
    user_list = User.objects.filter(
        date_joined__day=datetime.now().day,
    )
    user_list = User.objects.all()
    for user in user_list:
        if user.telegram_id:
            URL = 'https://api.telegram.org/bot'
            TOKEN = settings.TELEGRAM_TOKEN
            message = " Поздравляем с регистрацией на нашем сайте"
            response = requests.post(
                url=f'{URL}{TOKEN}/sendMessage',
                data={
                    'chat_id': user.telegram_id,
                    'text': message,
                }
            )
