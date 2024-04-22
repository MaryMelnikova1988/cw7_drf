import datetime
from datetime import datetime, date, timedelta

import requests
from celery import shared_task
from django.core.management import settings

from habits.models import Habit


@shared_task
def send_message_about_habits():
    time_now = datetime.now().time().replace(second=0, microsecond=0)
    date_now = date.today()
    # habits = Habit.objects.all().filter(time__lte=time_now)
    habits = Habit.objects.all()

    for habit in habits:
        print(habit.action)
        if habit.date is None:
            habit.date = date_now
        if habit.date == date_now:
            if habit.time == time_now:
                if habit.owner.telegram_id:
                    URL = 'https://api.telegram.org/bot'
                    TOKEN = settings.TELEGRAM_TOKEN
                    message = f'Тебе надо выполнить: {habit.action}, текущее время {time_now}'
                    # url = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage?chat_id={habit.owner.telegram_id}&text={message}'
                    requests.post(
                        url=f'{URL}{TOKEN}/sendMessage',
                        data={
                            'chat_id': habit.owner.telegram_id,
                            'text': message,
                        }
                    )
                    habit.date = date_now + timedelta(days=habit.periodicity)
                    habit.save()

# @shared_task
# def send_mess_hello():
#     user_list = User.objects.filter(
#         date_joined__day=datetime.now().day,
#     )
#     user_list = User.objects.all()
#     for user in user_list:
#         if user.telegram_id:
#             URL = 'https://api.telegram.org/bot'
#             TOKEN = settings.TELEGRAM_TOKEN
#             message = " Поздравляем с регистрацией на нашем сайте"
#             response = requests.post(
#                 url=f'{URL}{TOKEN}/sendMessage',
#                 data={
#                     'chat_id': user.telegram_id,
#                     'text': message,
#                 }
#             )
